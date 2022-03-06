EMPTY_PLAYER_COMBINED_DATA_META = {
    "pdga_number": None,
    "pdga_number_active": None,
    "crawl_datetime": None,
    "parse_datetime": None,
    "combined_datetime": None,
    "analyzed_datetime": None,
    "status_code": None,
    "failed_data_points": [],
}

EMPTY_PLAYER_COMBINED_DATA_GENERAL = {
    "player_name": None,
    "player_first_name": None,
    "player_middle_name": None,
    "player_last_name": None,
    "player_location": None,
    "player_country": None,
    "player_country_short": None,
    "player_state": None,
    "player_state_short": None,
    "player_city": None,
    "player_picture_url": None,
    "player_age": None,
    "player_age_estimate": None,
    "player_gender": None,
}

EMPTY_PLAYER_COMBINED_DATA_PDGA_DETAILS = {
    "player_classification": None,
    "player_classification_short": None,
    "player_member_since": None,
    "player_membership_status": None,
    "player_membership_status_expiration_date": None,
    "player_official_status": None,
    "player_official_status_boolean": None,
    "player_official_status_expiration_date": None,
    "player_upcoming_tournaments": [],
    "player_active_years": [],
    "player_inactive_years": [],
    "player_total_pdga_points": None,
}

EMPTY_PLAYER_COMBINED_DATA_RATING = {
    "player_rating": None,
    "player_rating_difference": None,
    "player_rating_updated": None,
    "player_rating_highest": None,
    "player_rating_highest_date": None,
    "player_rating_lowest": None,
    "player_rating_lowest_date": None,
    "player_highest_round_rating": None,
    "player_lowest_round_rating": None,
    "player_positive_tournament_rating_difference": None,
    "player_negative_tournament_rating_difference": None,
}

EMPTY_PLAYER_COMBINED_DATA_TOURNAMENTS = {
    "player_tournaments_attended": [],
    "player_tournaments_all": [],
    "player_tournaments_singles": [],
    "player_tournaments_doubles": [],
    "player_tournaments_team": [],
    "player_wins_all": None,
    "player_wins_singles": None,
    "player_wins_doubles": None,
    "player_wins_team": None,
    "player_money_won_all": None,
    "player_money_won_singles": None,
    "player_money_won_doubles": None,
    "player_money_won_team": None,
    "player_average_earnings_per_tournament_all": None,
    "player_average_earnings_per_tournament_singles": None,
    "player_average_earnings_per_tournament_doubles": None,
    "player_average_earnings_per_tournament_team": None,
    "player_highest_paid_event": {
        "tournament_id": None,
        "tournament_prize_money": None
    },
    "player_total_rounds_played_singles": None,
    "player_average_par": None,
    "player_average_final_placement": None,
    "player_tiers_played": {},
    "player_classifications_played": {},
    "player_total_rounds": None,
    "tournament_highest_par": None,
    "tournament_lowest_par": None,
}

EMPTY_PLAYER_COMBINED_DATA_ANALYTICS = {
    "player_tournaments_singles_yearly_average": None,
    "player_tournaments_singles_monthly_average": None,
    "player_wins_singles_yearly_average": None,
    "player_wins_singles_monthly_average": None,
    "player_tournaments_win_percentage_all": None,
    "player_tournaments_win_percentage_singles": None,
    "player_tournaments_win_percentage_doubles": None,
    "player_tournaments_win_percentage_team": None,
    "player_money_won_yearly_average": None,
    "player_money_won_monthly_average": None
}

EMPTY_PLAYER_COMBINED_DATA = {
    **EMPTY_PLAYER_COMBINED_DATA_META,
    **EMPTY_PLAYER_COMBINED_DATA_GENERAL,
    **EMPTY_PLAYER_COMBINED_DATA_PDGA_DETAILS,
    **EMPTY_PLAYER_COMBINED_DATA_RATING,
    **EMPTY_PLAYER_COMBINED_DATA_TOURNAMENTS,
    **EMPTY_PLAYER_COMBINED_DATA_ANALYTICS
}
