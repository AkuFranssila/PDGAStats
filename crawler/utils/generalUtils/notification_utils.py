def print_process_notification(current_value: int, total_value: int):
    percentile = float(current_value) / float(total_value)

    if (percentile in [0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90]):
        print(
            f'Current process {percentile * 100} done. Items processed {current_value}/{total_value}.')

    return percentile
