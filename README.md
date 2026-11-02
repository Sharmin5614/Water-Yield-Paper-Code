from pathlib import Path

# Replace these if your 1995 folder names differ
PRECIP_1995 = Path(
    r"E:\MYLSU\1.2_Seasonal_Water_Yield\1995\Precipitation_final"
)

ET0_1995 = Path(
    r"E:\MYLSU\1.2_Seasonal_Water_Yield\1995\FINAL_EVAPOTRANSPIRATION"
)

print("1995 PRECIPITATION FILES:")
if PRECIP_1995.exists():
    for f in sorted(PRECIP_1995.glob("*.tif")):
        print(f.name)
else:
    print("Folder not found:", PRECIP_1995)

print("\n1995 ET0 FILES:")
if ET0_1995.exists():
    for f in sorted(ET0_1995.glob("*.tif")):
        print(f.name)
else:
    print("Folder not found:", ET0_1995)
