import datetime


def calculate_max_timestamp(time_list):
    try:
        timestamp_list = []
        status = 0
        for times in time_list:
            try:
                dt = datetime.datetime.strptime(times, '%H:%M:%S')
                timestamp = dt.hour * 3600 + dt.minute * 60 + dt.second
                timestamp_list.append(timestamp)
            except Exception as e:
                status = 1
                timestamp_list.append(0)

        if sum(timestamp_list) == 0 and status == 0:
            return None
        return max(timestamp_list)
    except Exception as e:
        return None
