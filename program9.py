
import random
import serial
import time


COORDS = [(0,0,0), (1,1,0), (2,2,0), (3,3,0), (4,4,0), (5,5,0), (6,6,0), (7,7,0), (8,8,0), (9,9,0),
 (10,10,0), (11,11,0), (12,12,0), (13,13,0), (14,14,0), (15,15,0), (16,16,0), (17,17,0), (18,18,0), (19,19,0),
 (20,20,0), (21,21,0), (22,22,0), (23,23,0), (24,24,0), (25,25,0), (26,26,0), (27,27,0), (28,28,0), (29,29,0),
 (30,30,0), (31,31,0), (32,32,0), (33,33,0), (34,34,0), (35,35,0), (36,36,0), (37,37,0), (38,38,0), (39,39,0),
 (40,40,0), (41,41,0), (42,42,0), (43,43,0), (44,44,0), (45,45,0), (46,46,0), (47,47,0), (48,48,0), (49,49,0),
 (50,50,0), (51,51,0), (52,52,0), (53,53,0), (54,54,0), (55,55,0), (56,56,0), (57,57,0), (58,58,0), (59,59,0),
 (60,60,0), (61,61,0), (62,62,0), (63,63,0), (64,0,0), (65,1,1), (66,2,1), (67,3,1), (68,4,1), (69,5,1),
 (70,6,1), (71,7,1), (72,8,1), (73,9,1), (74,10,1), (75,11,1), (76,12,1), (77,13,1), (78,15,1), (79,16,1),
 (80,18,1), (81,19,1), (82,20,1), (83,22,1), (84,23,1), (85,25,1), (86,26,1), (87,27,1), (88,28,1), (89,30,1),
 (90,30,1), (91,31,1), (92,32,1), (93,33,1), (94,34,1), (95,36,1), (96,37,1), (97,38,1), (98,39,1), (99,40,1),
 (100,45,1), (101,46,1), (102,47,1), (103,48,1), (104,49,1), (105,49.25,1), (106,49.5,1), (107,50,1), (108,51,1), (109,53,1),
 (110,54,1), (111,56,1), (112,56,1), (113,58,1), (114,60,1), (115,61,1), (116,62,1), (117,63,1), (118,0,2), (119,2,2),
 (120,4,2), (121,4,2), (122,6,2), (123,6,2), (124,8,2), (125,10,2), (126,11,2), (127,12,2), (128,14,2), (129,14,2),
 (130,15,2), (131,17,2), (132,18,2), (133,19,2), (134,20,2), (135,21,2), (136,23,2), (137,24,2), (138,25,2), (139,27,2),
 (140,27,2), (141,28,2), (142,30,2), (143,31,2), (144,32,2), (145,33,2), (146,34,2), (147,35,2), (148,36,2), (149,37,2),
 (150,42,2), (151,43,2), (152,45,2), (153,45,2), (154,46,2), (155,48,2), (156,49,2), (157,49,2), (158,49.5,2), (159,50,2),
 (160,51,2), (161,53,2), (162,54,2), (163,55,2), (164,57,2), (165,58,2), (166,60,2), (167,61,2), (168,62,2), (169,63,2),
 (170,0,3), (171,1,3), (172,2,3), (173,4,3), (174,6,3), (175,6,3), (176,9,3), (177,9,3), (178,11,3), (179,12,3),
 (180,12,3), (181,14,3), (182,14,3), (183,16,3), (184,17,3), (185,18,3), (186,19,3), (187,21,3), (188,22,3), (189,24,3),
 (190,25,3), (191,26,3), (192,27,3), (193,27,3), (194,29,3), (195,29,3), (196,30,3), (197,31,3), (198,32,3), (199,33,3),
 (200,37,3), (201,38,3), (202,40,3), (203,41,3), (204,43,3), (205,45,3), (206,46,3), (207,48,3), (208,49,3), (209,49.5,3),
 (210,49.75,3), (211,51,3), (212,52,3), (213,53,3), (214,54,3), (215,55,3), (216,57,3), (217,58,3), (218,60,3), (219,60,3),
 (220,61,3), (221,62,3), (222,63,3), (223,1,4), (224,2,4), (225,4,4), (226,5,4), (227,6,4), (228,7,4), (229,8,4),
 (230,8,4), (231,10,4), (232,11,4), (233,13,4), (234,15,4), (235,16,4), (236,16,4), (237,17,4), (238,18,4), (239,20,4),
 (240,20,4), (241,21,4), (242,23,4), (243,25,4), (244,26,4), (245,28,4), (246,29,4), (247,29,4), (248,31,4), (249,31,4),
 (250,34,4), (251,36,4), (252,38,4), (253,39,4), (254,40,4), (255,43,4), (256,45,4), (257,46,4), (258,48,4), (259,49,4),
 (260,50,4), (261,51,4), (262,54,4), (263,54,4), (264,56,4), (265,57,4), (266,59,4), (267,60,4), (268,62,4), (269,63,4),
 (270,1,5), (271,2,5), (272,3,5), (273,6,5), (274,7,5), (275,8,5), (276,11,5), (277,11,5), (278,13,5), (279,13,5),
 (280,16,5), (281,16,5), (282,18,5), (283,20,5), (284,21,5), (285,23,5), (286,25,5), (287,27,5), (288,28,5), (289,29,5),
 (290,30,5), (291,32,5), (292,34,5), (293,37,5), (294,38,5), (295,41,5), (296,42,5), (297,46,5), (298,46,5), (299,49,5),
 (300,52,5), (301,53,5), (302,54,5), (303,58,5), (304,60,5), (305,62,5), (306,0,6), (307,1,6), (308,2,6), (309,4,6),
 (310,7,6), (311,8,6), (312,9,6), (313,12,6), (314,14,6), (315,17,6), (316,18,6), (317,20,6), (318,23,6), (319,24,6),
 (320,26,6), (321,27,6), (322,28,6), (323,31,6), (324,33,6), (325,35,6), (326,38,6), (327,41,6), (328,43,6), (329,46,6),
 (330,49.5,6), (331,49.75,6), (332,50,6), (333,53,6), (334,54,6), (335,56,6), (336,59,6), (337,61,6), (338,63,6), (339,0,7),
 (340,4,7), (341,6,7), (342,8,7), (343,11,7), (344,12,7), (345,15,7), (346,18,7), (347,19,7), (348,21,7), (349,23,7),
 (350,29,7), (351,30,7), (352,31,7), (353,34,7), (354,35,7), (355,38,7), (356,43,7), (357,46,7), (358,48,7), (359,49,7),
 (360,50,7), (361,53,7), (362,56,7), (363,58,7), (364,60,7), (365,62,7), (366,2,8), (367,3,8), (368,4,8), (369,6,8),
 (370,8,8), (371,10,8), (372,13,8), (373,15,8), (374,18,8), (375,20,8), (376,25,8), (377,26,8), (378,28,8), (379,32,8),
 (380,32,8), (381,37,8), (382,38,8), (383,42,8), (384,44,8), (385,48,8), (386,49,8), (387,50,8), (388,54,8), (389,57,8),
 (390,59,8), (391,61,8), (392,0,9), (393,4,9), (394,8,9), (395,8,9), (396,11,9), (397,12,9), (398,14,9), (399,18,9),
 (400,27,9), (401,30,9), (402,31,9), (403,34,9), (404,38,9), (405,39,9), (406,45,9), (407,49,9), (408,49.5,9), (409,53,9),
 (410,55,9), (411,58,9), (412,61,9), (413,1,10), (414,6,10), (415,6,10), (416,11,10), (417,12,10), (418,14,10), (419,19,10),
 (420,24,10), (421,26,10), (422,28,10), (423,33,10), (424,37,10), (425,40,10), (426,44,10), (427,49.5,10), (428,52,10), (429,54,10),
 (430,56,10), (431,59,10), (432,63,10), (433,2,11), (434,8,11), (435,8,11), (436,9,11), (437,14,11), (438,16,11), (439,20,11),
 (440,23,11), (441,26,11), (442,29,11), (443,30,11), (444,34,11), (445,38,11), (446,45,11), (447,45,11), (448,48,11), (449,54,11),
 (450,1,12), (451,1,12), (452,10,12), (453,15,12), (454,15,12), (455,23,12), (456,29,12), (457,29,12), (458,33,12), (459,33,13),
 (460,51,13), (461,61,13), (462,4,13), (463,4,12), (464,4,11), (465,4,11), (466,4,10), (467,4,10), (468,4,9), (469,4,9),
 (470,4,8), (471,4,8), (472,4,7), (473,4,7), (474,4,6.5), (475,4,6), (476,4,5.5), (477,4,5), (478,4,5), (479,4,4.5),
 (480,4,4), (481,4,3.5), (482,4,3), (483,4,3), (484,4,2), (485,4,2), (486,4,1.5), (487,4,1), (488,4,1), (489,4,.5), (490, 4, 0), (491, 4, 0)
]

COLORS = [(100, 0, 0), (0, 100, 0), (0, 0, 100), (125, 0, 125)]
PARTICLE_COLORS = COLORS

MAX_ROTATION = 64
MAX_LINE_LENGTH = 5
MAX_LINE = 13

ROTATION_TOLERANCE = 1

FLUSH_SLEEP  = .1


def find_light(rotation, line):
    if line > MAX_LINE:
        return -1
    for coord in COORDS:
        if coord[1] == rotation and coord[2] == line:
            return coord[0]
    for coord in COORDS:
        if abs(coord[1] - rotation) <= ROTATION_TOLERANCE and coord[2] == line:
            return coord[0]
    return -1

def find_lights_by_line(line):
    ret = []
    for coord in COORDS:
        if coord[2] == line:
            ret.append(coord[0])
    return ret

MAX_PARTICLES = 40
MIN_PARTICLES = 20
MAX_PARTICLE_LENGTH = 2
MIN_SPEED = .5
MAX_SPEED = 2
PARTICLE_CYCLES = 13

def generate_particles(light_state):
    particles = []
    for idx in range(random.randint(MIN_PARTICLES, MAX_PARTICLES)):
        if(light_state.exit_thread):
            helper.update()
            helper.flush()
            helper.clear()
            helper.flush()
            return
        particles.append([random.randint(0, MAX_ROTATION), random.randint(0, len(PARTICLE_COLORS)-1), (MAX_SPEED - MIN_SPEED) * random.random() + MIN_SPEED])
    return particles

HALO_LINE_COUNT = 4

def draw_halos(helper, light_state):
    for idx in range(HALO_LINE_COUNT):
        current_color = PARTICLE_COLORS[random.randint(0, len(PARTICLE_COLORS) - 1)]
        light_indexes = find_lights_by_line(MAX_LINE - idx)
        for light in light_indexes:
            if(light_state.exit_thread):
                helper.update()
                helper.flush()
                helper.clear()
                helper.flush()
                return
            helper.change(light, current_color[0], current_color[1], current_color[2])
        helper.update()
        helper.flush()
        time.sleep(FLUSH_SLEEP)
    time.sleep(2)

def draw_lines(helper, light_state):
    current_rotation = 0
    current_line = 0
    if(light_state.exit_thread):
        helper.update()
        helper.flush()
        helper.clear()
        helper.flush()
        return
    while True:
        if(light_state.exit_thread):
            helper.update()
            helper.flush()
            helper.clear()
            helper.flush()

            return
        lines = []
        current_color = 0
        for rot in range(current_rotation, MAX_ROTATION, int(MAX_ROTATION / len(COLORS))):
            for sub in range(MAX_LINE_LENGTH):
                if(light_state.exit_thread):
                    helper.update()
                    helper.flush()
                    helper.clear()
                    helper.flush()
                    return
                lines.append([rot, current_line-sub, current_color])
            current_color += 1
        for line in lines:
            light_index = find_light(line[0], line[1])
            if light_index != -1:
                if(light_state.exit_thread):
                    helper.update()
                    helper.flush()
                    helper.clear()
                    helper.flush()
                    return
                ci = line[2]
                r = COLORS[ci][0]
                g = COLORS[ci][1]
                b = COLORS[ci][2]
                helper.change(light_index, r, g, b)
        if(light_state.exit_thread):
            helper.update()
            helper.flush()
            helper.clear()
            helper.flush()
            return
        helper.update()
        helper.flush()
        time.sleep(.25)
        current_line += 1
        if current_line > MAX_LINE:
            break
    if(light_state.exit_thread):
        helper.update()
        helper.flush()
        helper.clear()
        helper.flush()
        return
    helper.clear()
    helper.update()
    helper.flush()
    time.sleep(FLUSH_SLEEP)


def create_lights_from_particle(particle, offset, light_state):
    ret = []
    if(light_state.exit_thread):
        helper.update()
        helper.flush()
        helper.clear()
        helper.flush()
        return
    for idx in range(MAX_PARTICLE_LENGTH):
        if(light_state.exit_thread):
            helper.update()
            helper.flush()
            helper.clear()
            helper.flush()
            return
        ret.append([particle[0], int(MAX_LINE + (MAX_PARTICLE_LENGTH + idx) - (offset * particle[2])), particle[1]])
    return ret


def draw_particles(helper, light_state):
    particle_definitions = generate_particles(light_state)
    offset = 0
    dimmer = 1
    if(light_state.exit_thread):
        helper.update()
        helper.flush()
        helper.clear()
        helper.flush()
        return
    while True:
        if(light_state.exit_thread):
            helper.update()
            helper.flush()
            helper.clear()
            helper.flush()
            return
        should_dim = False
        for particle in particle_definitions:
            if(light_state.exit_thread):
                helper.update()
                helper.flush()
                helper.clear()
                helper.flush()
                return
            lights = create_lights_from_particle(particle, offset, light_state)
            for l in lights:
                if(light_state.exit_thread):
                    helper.update()
                    helper.flush()
                    helper.clear()
                    helper.flush()
                    return
                light_index = find_light(l[0], l[1])
                if light_index != -1:
                    if(light_state.exit_thread):
                        helper.update()
                        helper.flush()
                        helper.clear()
                        helper.flush()
                        light_state.exit_thread = False
                        light_state.running = False
                        return
                    r = int(PARTICLE_COLORS[l[2]][0] * dimmer)
                    g = int(PARTICLE_COLORS[l[2]][1] * dimmer)
                    b = int(PARTICLE_COLORS[l[2]][2] * dimmer)
                    helper.change(light_index, r, g, b)
                    should_dim = True
        if(light_state.exit_thread):
            helper.update()
            helper.flush()
            helper.clear()
            helper.flush()
            return
        helper.update()
        if(light_state.exit_thread):
            helper.update()
            helper.flush()
            helper.clear()
            helper.flush()
            return
        helper.flush()
        time.sleep(.25)
        if offset > PARTICLE_CYCLES:
            break
        offset += 1
        if should_dim:
            dimmer *= .90
    if(light_state.exit_thread):
        helper.update()
        helper.flush()
        helper.clear()
        helper.flush()
        return
    helper.clear()
    helper.update()
    helper.flush()
    time.sleep(FLUSH_SLEEP)
    
    if(light_state.exit_thread):
        helper.update()
        helper.flush()
        helper.clear()
        helper.flush()
        return


def main(helper, num_lights, light_state):
    light_state.running = True
    helper.clear()
    while True:
        if(light_state.exit_thread):
            helper.update()
            helper.flush()
            helper.clear()
            helper.flush()
            light_state.exit_thread = False
            light_state.running = False
            return
        draw_lines(helper, light_state)
        
        if(light_state.exit_thread):
            helper.update()
            helper.flush()
            helper.clear()
            helper.flush()
            light_state.exit_thread = False
            light_state.running = False
            return
        draw_halos(helper, light_state)
        if(light_state.exit_thread):
            helper.update()
            helper.flush()
            helper.clear()
            helper.flush()
            light_state.exit_thread = False
            light_state.running = False
            return
        draw_particles(helper, light_state)

        if(light_state.exit_thread):
            helper.update()
            helper.flush()
            helper.clear()
            helper.flush()
            light_state.exit_thread = False
            light_state.running = False
            return


# if __name__ == "__main__":
#     main(HelperMock(), 500, LightState())
