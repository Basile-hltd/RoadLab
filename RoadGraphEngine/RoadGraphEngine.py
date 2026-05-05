import sys
import OSM_Access.OSM_Access as OSM_Access

arg_list = sys.argv

if len(arg_list) != 4:
    print("-- Invalid argument list --")
    exit()

print("=== Program Start ===")

try:
    lat = float(arg_list[1])
    lon = float(arg_list[2])
    dia = float(arg_list[3])

except:
    print("-- Invalid argument list --")
    exit()

print("Latitude \t:", lat, "\t", type(lat))
print("Longitude \t:", lon, "\t", type(lon))
print("Diameter \t:", dia, "\t", type(dia))

api_version = OSM_Access.Version()

if api_version == None:
    print("-- API error --")
    exit()

print("\nOpen Street Map API reachable\t Version :", api_version)

if(not OSM_Access.GetTile(lat, lon, 1000)):
   print("GetTileError")