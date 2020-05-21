from helper import read_tba
from helper import utils

def getTeamInfo(number):
    data = read_tba.get("team/frc"+str(number)+"/simple")
    name, state, country = data["nickname"], data["state_prov"], data["country"]
    region = state if country=="USA" else country

    years = len(read_tba.get("team/frc"+str(number)+"/years_participated"))

    try: district = read_tba.get("team/frc"+str(number)+"/districts")[-1]["abbreviation"]
    except Exception as e: district = "None"

    return [name, region, district, years]

def saveAllTeamsInfo():
    out = {}
    for team in utils.loadAllTeams():
        out[team] = getTeamInfo(team)
        print(out[team])
    utils.saveAllTeamsInfo(out)

states = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

districts = {
    "mar": "fma",
    "nc": "fnc",
    "tx": "fit",
    "in": "fin",

}

def cleanTeamInfo():
    teams = utils.loadAllTeamsInfo()
    for team in teams:
        data = teams[team]
        if(data[1] in states): data[1] = states[data[1]]
        if(data[2] in districts): data[2] = districts[data[2]]
        teams[team] = data
    utils.saveAllTeamsInfo(teams)


if __name__ == "__main__":
    #saveAllTeamsInfo()
    #cleanTeamInfo()
    print(utils.loadAllTeamsInfo())
