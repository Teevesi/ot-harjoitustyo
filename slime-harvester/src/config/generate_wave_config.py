
def generate_wave_config(max_wave=50):
    wave_config = {}

    for wave in range(1, max_wave + 1):
        # Boss waves every 10th wave after wave 10
        if wave % 10 == 0:
            wave_config[wave] = boss_wave(wave)
            continue

        # Determine slime tier
        if wave <= 10:
            slime = "red_slime"
        elif wave <= 20:
            slime = "blue_slime"
        elif wave <= 35:
            slime = "green_slime"
        else:
            slime = "pink_slime"

        # Enemy count scaling
        enemy_count = int(5 + wave * 2.5)

        # Spawn interval scaling (clamped)
        spawn_interval = max(5, 20 - wave // 3)

        wave_config[wave] = {
            "enemy_count": enemy_count,
            "spawn_interval": spawn_interval,
            "enemy_type": slime
        }

    return wave_config

def endless_wave(wave_number):
    difficulty_multiplier = wave_number - 50

    enemy_count = int(130 + difficulty_multiplier * 5)
    spawn_interval = max(3, 5 - difficulty_multiplier // 10)

    enemy_type = "pink_slime"
    if wave_number % 10 == 0:
        return boss_wave(wave_number)

    return {
        "enemy_count": enemy_count,
        "spawn_interval": spawn_interval,
        "enemy_type": enemy_type
    }

def boss_wave(wave_number):
    enemy_count = max(1, (wave_number // 10) - 1)
    spawn_interval = 60

    return {
        "enemy_count": enemy_count,
        "spawn_interval": spawn_interval,
        "enemy_type": "boss_rainbow"
    }
