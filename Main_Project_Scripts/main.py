import district

def get_district_data(districtList):
    ans = ''
    for district in districtList:
        ans += f'{district.name}\n'
    return ans