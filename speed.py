import time
import psutil

def measure_disk_speed(duration=10):
    start_time = time.time()
    end_time = start_time + duration
    bytes_read_start = psutil.disk_io_counters().read_bytes
    bytes_written_start = psutil.disk_io_counters().write_bytes

    while time.time() < end_time:
        time.sleep(1)

    bytes_read_end = psutil.disk_io_counters().read_bytes
    bytes_written_end = psutil.disk_io_counters().write_bytes

    read_speed = (bytes_read_end - bytes_read_start) / duration
    write_speed = (bytes_written_end - bytes_written_start) / duration

    return read_speed, write_speed

if __name__ == "__main__":
    duration = 10  # Measurement duration in seconds
    read_speed, write_speed = measure_disk_speed(duration)

    print(f"Read speed: {read_speed / (1024 * 1024):.2f} MB/s")
    print(f"Write speed: {write_speed / (1024 * 1024):.2f} MB/s")
