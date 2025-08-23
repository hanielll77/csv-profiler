import argparse
from pathlib import Path
from .core import profile_csv, clean_csv

def main():
    p = argparse.ArgumentParser(prog="csv-profiler", description="CSV profiler & cleaner")
    p.add_argument("input", help="Path to CSV file")
    p.add_argument("--out", default="clean.csv", help="Output cleaned CSV path")
    p.add_argument("--no-dedup", action="store_true", help="Do not drop duplicate rows")
    p.add_argument("--profile", default="profile.csv", help="Save profile summary (CSV)")
    args = p.parse_args()

    inp = Path(args.input)

    prof = profile_csv(inp)
    prof.to_csv(args.profile, index=True)

    cleaned = clean_csv(inp, drop_duplicates=not args.no_dedup)
    cleaned.to_csv(args.out, index=False)

    print(f"✅ Profile saved to {args.profile}")
    print(f"✅ Cleaned CSV saved to {args.out}")

if __name__ == "__main__":
    main()
