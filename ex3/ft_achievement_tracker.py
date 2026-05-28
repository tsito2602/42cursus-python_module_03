import random

ACHIEVEMENTS = [
    "Crafting Genius",
    "World Savior",
    "Master Explorer",
    "Collector Supreme",
    "Untouchable",
    "Boss Slayer",
    "Strategist",
    "Unstoppable",
    "Speed Runner",
    "Survivor",
    "Treasure Hunter",
    "First Steps",
    "Sharp Mind",
    "Hidden Path Finder",
]
MIN_PLAYERS = 5
MAX_PLAYERS = 10


def gen_player_achievements() -> set[str]:
    count = random.randint(MIN_PLAYERS, MAX_PLAYERS)
    player_achievements = random.sample(ACHIEVEMENTS, count)
    return set(player_achievements)


def main() -> None:
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    achievements = set(ACHIEVEMENTS)
    all_distinct = set.union(alice, bob, charlie, dylan)

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print(f"\nAll distinct achievements: {all_distinct}")
    print(
        f"\nCommon achievements: "
        f"{set.intersection(alice, bob, charlie, dylan)}"
    )
    print(f"\nOnly Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}")
    print(f"\nAlice is missing: {achievements.difference(alice)}")
    print(f"Bob is missing: {achievements.difference(bob)}")
    print(f"Charlie is missing: {achievements.difference(charlie)}")
    print(f"Dylan is missing: {achievements.difference(dylan)}")


if __name__ == "__main__":
    main()
