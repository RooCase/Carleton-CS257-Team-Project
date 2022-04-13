import district

def list_districts(districtList):
    ans = ''
    for district in districtList:
        ans += f'{district.name}\n'
    return ans
