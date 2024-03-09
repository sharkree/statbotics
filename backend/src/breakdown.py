from typing import Dict, List

from src.constants import CURR_YEAR

key_to_name = {
    2016: {
        "auto": "auto_points",
        "teleop": "teleop_points",
        "endgame": "endgame_points",
        "rp_1": "defenses_rp",
        "rp_2": "tower_rp",
        "tiebreaker": "tiebreaker_points",
        "comp_1": "auto_reach_points",
        "comp_2": "auto_crossing_points",
        "comp_3": "auto_low_boulders",
        "comp_4": "auto_high_boulders",
        "comp_5": "teleop_crossing_points",
        "comp_6": "teleop_low_boulders",
        "comp_7": "teleop_high_boulders",
        "comp_8": "challenge_points",
        "comp_9": "scale_points",
        "comp_10": "defenses",
        "comp_11": "boulders",
    },
    2017: {
        "auto": "auto_points",
        "teleop": "teleop_points",
        "endgame": "endgame_points",
        "rp_1": "rotor_rp",
        "rp_2": "kpa_rp",
        "tiebreaker": "tiebreaker_points",
        "comp_1": "auto_mobility_points",
        "comp_2": "auto_fuel_low",
        "comp_3": "auto_fuel_high",
        "comp_4": "auto_rotor_points",
        "comp_5": "teleop_fuel_low",
        "comp_6": "teleop_fuel_high",
        "comp_7": "teleop_rotor_points",
        "comp_8": "takeoff_points",
        "comp_9": "kpa",
        "comp_10": "gears",
    },
    2018: {
        "auto": "auto_points",
        "teleop": "teleop_points",
        "endgame": "endgame_points",
        "rp_1": "auto_rp",
        "rp_2": "climb_rp",
        "tiebreaker": "tiebreaker_points",
        "comp_1": "auto_run_points",
        "comp_2": "auto_switch_secs",
        "comp_3": "auto_scale_secs",
        "comp_4": "teleop_switch_secs",
        "comp_5": "teleop_scale_secs",
        "comp_6": "vault_points",
        "comp_7": "auto_scale_power",
        "comp_8": "switch_power",
        "comp_9": "scale_power",
        "comp_10": "opp_switch_power",
    },
    2019: {
        "auto": "auto_points",
        "teleop": "teleop_points",
        "endgame": "endgame_points",
        "rp_1": "rocket_rp",
        "rp_2": "hab_rp",
        "tiebreaker": "tiebreaker_points",
        "comp_1": "sandstorm_points",
        "comp_2": "bay_hatch_pieces",
        "comp_3": "bay_cargo_pieces",
        "comp_4": "rocket_hatch_low_pieces",
        "comp_5": "rocket_hatch_mid_pieces",
        "comp_6": "rocket_hatch_high_pieces",
        "comp_7": "rocket_cargo_low_pieces",
        "comp_8": "rocket_cargo_mid_pieces",
        "comp_9": "rocket_cargo_high_pieces",
        "comp_10": "hab_climb_points",
        "comp_11": "rocket_pieces",
        "comp_12": "bay_pieces",
    },
    2020: {
        "auto": "auto_points",
        "teleop": "teleop_points",
        "endgame": "endgame_points",
        "rp_1": "cells_rp",
        "rp_2": "climb_rp",
        "tiebreaker": "tiebreaker_points",
        "comp_1": "auto_init_line_points",
        "comp_2": "auto_cells_bottom",
        "comp_3": "auto_cells_outer",
        "comp_4": "auto_cells_inner",
        "comp_5": "teleop_cells_bottom",
        "comp_6": "teleop_cells_outer",
        "comp_7": "teleop_cells_inner",
        "comp_8": "control_panel_points",
        "comp_9": "endgame_points",
        "comp_10": "cells",
    },
    2021: {},
    2022: {
        "auto": "auto_points",
        "teleop": "teleop_points",
        "endgame": "endgame_points",
        "rp_1": "cargo_rp",
        "rp_2": "hangar_rp",
        "tiebreaker": "tiebreaker_points",
        "comp_1": "auto_taxi_points",
        "comp_2": "auto_cargo_lower",
        "comp_3": "auto_cargo_upper",
        "comp_4": "teleop_cargo_lower",
        "comp_5": "teleop_cargo_upper",
        "comp_6": "endgame_points",
        "comp_7": "cargo",
    },
    2023: {
        "auto": "auto_points",
        "teleop": "teleop_points",
        "endgame": "endgame_points",
        "rp_1": "links_rp",
        "rp_2": "activation_rp",
        "tiebreaker": "tiebreaker_points",
        "comp_1": "auto_charge_station_points",
        "comp_2": "auto_pieces",
        "comp_3": "auto_grid_points",
        "comp_4": "teleop_pieces",
        "comp_5": "teleop_grid_points",
        "comp_6": "bottom_pieces",
        "comp_7": "middle_pieces",
        "comp_8": "top_pieces",
        "comp_9": "cubes_scored",
        "comp_10": "cube_points",
        "comp_11": "cones_scored",
        "comp_12": "cone_points",
        "comp_13": "total_pieces",
        "comp_14": "links",
        "comp_15": "grid_points",
        "comp_16": "endgame_charge_station_points",
    },
    2024: {
        "auto": "auto_points",
        "teleop": "teleop_points",
        "endgame": "endgame_points",
        "rp_1": "melody_rp",
        # TODO: Rename to ensemble_rp
        "rp_2": "harmony_rp",
        "tiebreaker": "tiebreaker_points",
        "comp_1": "auto_leave_points",
        "comp_2": "auto_notes",
        "comp_3": "auto_note_points",
        "comp_4": "teleop_notes",
        "comp_5": "teleop_note_points",
        "comp_6": "amp_notes",
        "comp_7": "amp_points",
        "comp_8": "speaker_notes",
        "comp_9": "speaker_points",
        "comp_10": "amplified_notes",
        "comp_11": "total_notes",
        "comp_12": "total_note_points",
        "comp_13": "endgame_park_points",
        "comp_14": "endgame_on_stage_points",
        "comp_15": "endgame_harmony_points",
        "comp_16": "endgame_trap_points",
        "comp_17": "endgame_spotlight_points",
    },
}

all_keys: Dict[int, List[str]] = {}
for year in range(2002, CURR_YEAR + 1):
    if year not in key_to_name:
        all_keys[year] = ["no_foul_points"]
    else:
        all_keys[year] = [
            "no_foul_points",
            "auto_points",
            "teleop_points",
            "endgame_points",
            "rp_1",
            "rp_2",
            "tiebreaker_points",
        ]
        for i in range(1, 18):
            if f"comp_{i}" in key_to_name[year]:
                all_keys[year].append(key_to_name[year][f"comp_{i}"])
