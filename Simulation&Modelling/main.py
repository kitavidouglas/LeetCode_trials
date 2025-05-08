import math
import random

# Server states
SERVER_IDLE = 0
SERVER_BUSY = 1

# System limits and a constant to represent “infinity”
MAX_QUEUE_SIZE = 100
FAR_FUTURE_TIME = 1.0e+30

# Simulation clock and event times
current_time = 0.0
last_event_time = 0.0
cumulative_queue_time = 0.0
cumulative_busy_time = 0.0

# Counters for customers and delays
customers_served = 0
total_delay_time = 0.0
queue_length = 0
server_status = SERVER_IDLE

# Schedule for the next events: 1 -> arrival, 2 -> departure
scheduled_events = {1: 0.0, 2: FAR_FUTURE_TIME}

# List to store arrival times for customers waiting in line
waiting_arrivals = [0.0] * (MAX_QUEUE_SIZE + 1)

# Input parameters (to be loaded from file)
interarrival_mean = 0.0
service_mean = 0.0
required_customers = 0

# Variable to keep track of which event is next
upcoming_event = None

def generate_exponential(mean_value):
    """
    Generate an exponentially distributed random time
    """
    return -mean_value * math.log(random.random())

def initialize_simulation():
    """
    Reset simulation variables and schedule the first arrival.
    """
    global current_time, last_event_time, customers_served, total_delay_time, queue_length, server_status, scheduled_events
    current_time = 0.0
    last_event_time = 0.0
    customers_served = 0
    total_delay_time = 0.0
    queue_length = 0
    server_status = SERVER_IDLE

    # Schedule the first arrival event; departure remains far in the future initially.
    scheduled_events[1] = current_time + generate_exponential(interarrival_mean)
    scheduled_events[2] = FAR_FUTURE_TIME

def determine_next_event():
    """
    Choose the next event (arrival or departure) based on which has the smallest scheduled time.
    Update the simulation clock accordingly.
    """
    global current_time, upcoming_event
    min_time = FAR_FUTURE_TIME
    upcoming_event = None

    for event_type, event_time in scheduled_events.items():
        if event_time < min_time:
            min_time = event_time
            upcoming_event = event_type

    # No valid event found: this should not happen
    if upcoming_event is None:
        raise RuntimeError(f"No upcoming event found at time {current_time}")

    current_time = scheduled_events[upcoming_event]

def update_statistics():
    """
    Update the time-average statistics based on the time since the last event.
    """
    global last_event_time, cumulative_queue_time, cumulative_busy_time, queue_length, server_status, current_time
    time_since_last = current_time - last_event_time
    last_event_time = current_time
    cumulative_queue_time += queue_length * time_since_last
    cumulative_busy_time += server_status * time_since_last


def handle_arrival():
    """
    Process an arrival event:
      - Schedule the next arrival.
      - If the server is busy, add the customer to the queue.
      - If the server is idle, start service immediately.
    """
    global scheduled_events, queue_length, server_status, customers_served, total_delay_time, waiting_arrivals

    # Schedule the next arrival.
    scheduled_events[1] = current_time + generate_exponential(interarrival_mean)

    if server_status == SERVER_BUSY:
        # Increment the queue length.
        queue_length += 1
        if queue_length > MAX_QUEUE_SIZE:
            raise OverflowError(f"Queue overflow at time {current_time}")
        waiting_arrivals[queue_length] = current_time
    else:
        # No waiting; service starts immediately.
        total_delay_time += 0.0  # Immediate service, zero delay.
        customers_served += 1
        server_status = SERVER_BUSY
        scheduled_events[2] = current_time + generate_exponential(service_mean)

def handle_departure():
    """
    Process a departure event:
      - If the queue is empty, mark the server as idle.
      - Otherwise, dequeue the first customer, calculate their delay, and schedule the next departure.
    """
    global queue_length, server_status, customers_served, total_delay_time, waiting_arrivals, scheduled_events

    if queue_length == 0:
        # No customers waiting: set the server idle.
        server_status = SERVER_IDLE
        scheduled_events[2] = FAR_FUTURE_TIME
    else:
        # Customer from the queue begins service.
        delay = current_time - waiting_arrivals[1]
        total_delay_time += delay
        customers_served += 1

        # Schedule the departure for this customer.
        scheduled_events[2] = current_time + generate_exponential(service_mean)

        # Shift the waiting list up by one.
        for i in range(1, queue_length):
            waiting_arrivals[i] = waiting_arrivals[i + 1]
        queue_length -= 1

# Reporting and Main Simulation Loop
def output_report(filename):
    """
    Compute performance metrics and write the simulation report to the specified file.
    """
    with open(filename, "w") as report_file:
        report_file.write("Single-Server Queue Simulation Report\n\n")
        avg_delay = total_delay_time / customers_served if customers_served > 0 else 0.0
        avg_queue_length = cumulative_queue_time / current_time if current_time > 0 else 0.0
        utilization = cumulative_busy_time / current_time if current_time > 0 else 0.0

        report_file.write(f"Average delay in queue: {avg_delay:.3f} minutes\n")
        report_file.write(f"Average number in queue: {avg_queue_length:.3f}\n")
        report_file.write(f"Server utilization: {utilization:.3f}\n")
        report_file.write(f"Total simulation time: {current_time:.3f} minutes\n")

def run_simulation():
    """
    Main simulation routine:
      - Load simulation parameters.
      - Initialize the simulation.
      - Process events until the required number of customers have been served.
      - Output the final simulation report.
    """
    global interarrival_mean, service_mean, required_customers

    # Read simulation parameters from the external file.
    with open("mm1.in", "r") as infile:
        params = infile.readline().split()
        interarrival_mean = float(params[0])
        service_mean = float(params[1])
        required_customers = int(float(params[2]))

    # Write a header to the output file before starting the simulation.
    with open("mm1.out", "w") as init_out:
        init_out.write("Single-Server Queue Simulation\n\n")
        init_out.write(f"Mean interarrival time: {interarrival_mean:.3f} minutes\n")
        init_out.write(f"Mean service time:      {service_mean:.3f} minutes\n")
        init_out.write(f"Number of customers:    {required_customers:d}\n\n")

    # Initialize simulation variables and schedule the first arrival.
    initialize_simulation()

    # Continue the simulation loop until the desired number of customers are served.
    while customers_served < required_customers:
        determine_next_event()
        update_statistics()

        if upcoming_event == 1:
            handle_arrival()
        elif upcoming_event == 2:
            handle_departure()

    # After the simulation, generate and write the report.
    output_report("mm1.out")

# Entry Point

if __name__ == "__main__":
    run_simulation()
