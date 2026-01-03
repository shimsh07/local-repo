import os, sys

def parse(s):
    nums = []
    for x in s.replace(",", " ").split():
        try:
            nums.append(float(x))
        except:
            print(f"warning: skipping non-numeric token: {x}")
    return nums

def read_scores():
    if len(sys.argv) > 1:
        return parse(" ".join(sys.argv[1:]))
    if os.getenv("SCORES"):
        return parse(os.getenv("SCORES"))
    if os.path.isfile("scores.txt"):
        return parse(open("scores.txt").read())
    return parse(input("Enter scores separated by spaces or commas: "))

def main():
    scores = read_scores()
    if not scores:
        print("No valid scores provided.")
        sys.exit(1)

    print("=== main/master branch output ===")
    print(f"Count of scores: {len(scores)}")
    print(f"Sum: {sum(scores)}")
    print(f"Average: {sum(scores)/len(scores)}")
    print("\n=== local branch output (max & min) ===")
    print(f"Maximum: {max(scores)}")
    print(f"Minimum: {min(scores)}")
if __name__ == "__main__":
    main()
