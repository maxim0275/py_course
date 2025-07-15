from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(filter_state_src_list: list, filter_state_param_filter: str, filter_state_dst_list: list) -> None :
    assert filter_by_state(filter_state_src_list, filter_state_param_filter) == filter_state_dst_list


def test_sort_by_date(sort_by_date_src_list: list, sort_by_date_dst_list: list) -> None :
    assert sort_by_date(sort_by_date_src_list) == sort_by_date_dst_list
