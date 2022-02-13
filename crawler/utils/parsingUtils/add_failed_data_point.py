def add_failed_data_point(data: dict, data_point_name: str) -> None:
    failed_data_points = {"failed_data_points": [data_point_name]}

    data.update(failed_data_points)
