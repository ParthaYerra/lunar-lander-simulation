
import pygame
import math
import random

pygame.init()

WIDTH, HEIGHT = 1100, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("LUNAR | Autonomous Landing Simulation")
clock = pygame.time.Clock()

# Colors
SPACE = (7, 11, 23)
WHITE = (232, 238, 247)
MUTED = (133, 151, 177)
CYAN = (92, 210, 235)
ORANGE = (255, 166, 75)
GREEN = (89, 225, 157)
RED = (255, 100, 105)
PANEL = (16, 25, 43)
LINE = (40, 61, 84)

font = pygame.font.SysFont("consolas", 20)
small = pygame.font.SysFont("consolas", 15)
tiny = pygame.font.SysFont("consolas", 12)
title_font = pygame.font.SysFont("consolas", 25, bold=True)

# Physics
gravity = 1.62
mass = 1000.0
max_thrust = 3000.0
dt = 0.1

def reset_simulation():
    global altitude, velocity, flight_time
    global throttle, landed, crashed, impact_velocity

    altitude = 100.0
    velocity = -5.0
    flight_time = 0.0
    throttle = 0.0
    landed = False
    crashed = False
    impact_velocity = None

reset_simulation()

# Scene
GROUND_Y = 570
LANDER_X = 520
PIXELS_PER_METER = 4.0

random.seed(14)

stars = [
    (random.randrange(WIDTH), random.randrange(20, 500),
     random.choice([1, 1, 1, 2]))
    for _ in range(150)
]

horizon = [
    (x, GROUND_Y + random.randint(-8, 8))
    for x in range(-30, WIDTH + 60, 30)
]

craters = [
    (random.randint(20, WIDTH - 20),
     random.randint(GROUND_Y + 30, HEIGHT - 10),
     random.randint(12, 40))
    for _ in range(24)
]

def draw_text(message, x, y, color=WHITE, font_obj=font):
    screen.blit(font_obj.render(message, True, color), (x, y))

def draw_panel(rect):
    pygame.draw.rect(screen, PANEL, rect, border_radius=9)
    pygame.draw.rect(screen, LINE, rect, 1, border_radius=9)

def draw_lander(x, y, flame_on, power):
    # Ground shadow
    pygame.draw.ellipse(
        screen, (49, 52, 61),
        (x - 36, GROUND_Y - 5, 72, 10)
    )

    # THRUSTER FLAME: responds directly to throttle
    if flame_on and power > 0:
        strength = max(0.0, min(1.0, power / 100.0))

        # More throttle means a longer and wider flame.
        # Random flicker makes the flame look active.
        flicker = random.uniform(0.85, 1.15)
        flame_length = int((8 + 85 * strength) * flicker)
        flame_width = int(2 + 13 * strength)

        # Outer flame
        pygame.draw.polygon(screen, (230, 65, 30), [
            (x - flame_width, y + 27),
            (x + flame_width, y + 27),
            (x, y + 27 + flame_length)
        ])

        # Orange flame core
        pygame.draw.polygon(screen, (255, 145, 35), [
            (x - max(1, flame_width * 2 // 3), y + 27),
            (x + max(1, flame_width * 2 // 3), y + 27),
            (x, y + 27 + int(flame_length * 0.72))
        ])

        # Bright center appears at higher throttle
        if strength > 0.25:
            pygame.draw.polygon(screen, (255, 225, 150), [
                (x - max(1, flame_width // 4), y + 27),
                (x + max(1, flame_width // 4), y + 27),
                (x, y + 27 + int(flame_length * 0.38))
            ])

    # Landing struts
    pygame.draw.lines(
        screen, (175, 188, 201), False,
        [(x - 12, y + 14), (x - 29, y + 37),
         (x - 37, y + 37)], 4
    )
    pygame.draw.lines(
        screen, (175, 188, 201), False,
        [(x + 12, y + 14), (x + 29, y + 37),
         (x + 37, y + 37)], 4
    )

    # Main spacecraft body
    pygame.draw.polygon(screen, (184, 194, 204), [
        (x - 18, y - 10), (x - 13, y - 25),
        (x + 13, y - 25), (x + 18, y - 10),
        (x + 14, y + 18), (x - 14, y + 18)
    ])

    # Upper body shading
    pygame.draw.polygon(screen, (102, 126, 145), [
        (x - 13, y - 22), (x + 13, y - 22),
        (x + 9, y - 10), (x - 9, y - 10)
    ])

    pygame.draw.rect(
        screen, (69, 100, 119),
        (x - 8, y - 20, 16, 8), border_radius=2
    )

    # Gold thermal blanket details
    pygame.draw.line(
        screen, (232, 177, 91),
        (x - 13, y + 2), (x + 13, y + 2), 2
    )
    pygame.draw.circle(screen, CYAN, (x, y - 15), 3)

    # Landing feet
    pygame.draw.line(
        screen, WHITE, (x - 43, y + 38), (x - 30, y + 38), 3
    )
    pygame.draw.line(
        screen, WHITE, (x + 30, y + 38), (x + 43, y + 38), 3
    )

def draw_scene():
    screen.fill(SPACE)

    # Stars
    for sx, sy, radius in stars:
        pygame.draw.circle(screen, (160, 177, 202), (sx, sy), radius)

    # Lunar surface
    pygame.draw.rect(
        screen, (72, 77, 88),
        (0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y)
    )
    pygame.draw.polygon(
        screen, (101, 106, 117),
        [(0, GROUND_Y)] + horizon + [(WIDTH, HEIGHT), (0, HEIGHT)]
    )
    pygame.draw.lines(screen, (171, 176, 184), False, horizon, 2)

    # Craters
    for cx, cy, radius in craters:
        crater_rect = (
            cx - radius, cy - radius // 3,
            radius * 2, int(radius * 0.65)
        )
        pygame.draw.ellipse(screen, (74, 79, 90), crater_rect)
        pygame.draw.arc(
            screen, (135, 140, 150), crater_rect,
            0.1, math.pi - 0.1, 2
        )

    # Header
    draw_text("LUNAR", 28, 20, CYAN, title_font)
    draw_text("/ AUTONOMOUS LANDING SYSTEM", 137, 26, WHITE, small)
    pygame.draw.line(screen, LINE, (28, 61), (WIDTH - 28, 61), 1)

    # Telemetry panel
    draw_panel((28, 82, 285, 250))
    draw_text("FLIGHT TELEMETRY", 45, 98, CYAN, small)
    pygame.draw.line(screen, LINE, (45, 123), (294, 123))

    draw_text("ALTITUDE", 45, 140, MUTED, tiny)
    draw_text(f"{altitude:7.2f} m", 45, 158, WHITE)

    draw_text("VERTICAL VELOCITY", 45, 194, MUTED, tiny)
    draw_text(f"{velocity:7.2f} m/s", 45, 212, WHITE)

    draw_text("ENGINE THROTTLE", 45, 248, MUTED, tiny)
    draw_text(f"{throttle:5.1f}%", 45, 266, ORANGE, small)

    pygame.draw.rect(
        screen, LINE, (45, 293, 248, 7), border_radius=3
    )
    pygame.draw.rect(
        screen, ORANGE,
        (45, 293, int(248 * throttle / 100), 7),
        border_radius=3
    )

    # Mission panel
    draw_panel((WIDTH - 285, 82, 257, 170))
    draw_text("MISSION STATUS", WIDTH - 265, 98, CYAN, small)
    pygame.draw.line(
        screen, LINE, (WIDTH - 265, 123), (WIDTH - 48, 123)
    )
    draw_text(f"TIME  {flight_time:7.1f} s",
              WIDTH - 265, 141, WHITE, small)
    draw_text(f"GRAVITY {gravity:.2f} m/s²",
              WIDTH - 265, 169, WHITE, small)
    draw_text(f"THRUST {max_thrust:.0f} N",
              WIDTH - 265, 197, WHITE, small)

    # Landing target
    pygame.draw.line(
        screen, (108, 132, 149),
        (LANDER_X - 55, GROUND_Y),
        (LANDER_X + 55, GROUND_Y), 2
    )
    pygame.draw.line(
        screen, CYAN,
        (LANDER_X - 20, GROUND_Y + 5),
        (LANDER_X + 20, GROUND_Y + 5), 2
    )

    # Position lander based on altitude
    lander_y = GROUND_Y - 38 - int(altitude * PIXELS_PER_METER)
    lander_y = max(100, lander_y)

    draw_lander(
        LANDER_X, lander_y,
        not landed and not crashed and throttle > 0,
        throttle
    )

    # Status banner
    if crashed:
        status, status_color = "CRASH / IMPACT TOO HIGH", RED
    elif landed:
        status, status_color = "SAFE LANDING / TOUCHDOWN", GREEN
    else:
        status, status_color = "AUTOPILOT ENGAGED", CYAN

    draw_panel((28, 355, 360, 70))
    draw_text(status, 45, 368, status_color, small)

    if landed:
        draw_text(
            f"Impact speed: {abs(impact_velocity):.2f} m/s",
            45, 393, status_color, small
        )
    elif crashed:
        draw_text(
            f"Impact speed: {abs(impact_velocity):.2f} m/s",
            45, 393, status_color, small
        )
    else:
        draw_text(
            "Target: controlled vertical descent",
            45, 393, MUTED, tiny
        )

    draw_text("R / RESTART     ESC / EXIT",
              28, HEIGHT - 25, MUTED, tiny)

# Main simulation loop
running = True

while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_r:
                reset_simulation()

    # Autonomous flight controller
    if not landed and not crashed:
        target_velocity = -min(5.0, max(0.5, altitude * 0.15))

        desired_acceleration = 0.8 * (target_velocity - velocity)
        required_thrust = mass * (gravity + desired_acceleration)

        throttle = max(
            0.0,
            min(100.0, 100 * required_thrust / max_thrust)
        )

        actual_thrust = max_thrust * throttle / 100
        acceleration = actual_thrust / mass - gravity

        old_altitude = altitude
        velocity += acceleration * dt
        altitude += velocity * dt
        flight_time += dt

        # Detect touchdown and preserve impact velocity
        if altitude <= 0:
            fraction = old_altitude / (old_altitude - altitude)
            impact_velocity = velocity

            flight_time -= dt * (1 - fraction)
            altitude = 0.0

            landed = True
            crashed = abs(impact_velocity) > 3.0

    draw_scene()
    pygame.display.flip()

pygame.quit()
