#! /usr/bin/env python3
#Note: Write a solution with O(n) time complexity and O(1) additional space complexity, since this is what you would be asked to do during a real interview.

#Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return -1.

#Example

#For a = [2, 3, 3, 1, 5, 2], the output should be
#firstDuplicate(a) = 3.

#There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller index than than second occurrence of 2 does, so the answer is 3.

#For a = [2, 4, 3, 5, 1], the output should be
#firstDuplicate(a) = -1.

#Input/Output

#[time limit] 4000ms (py3)
#[input] array.integer a

#Guaranteed constraints:
#1 ≤ a.length ≤ 105,
#1 ≤ a[i] ≤ a.length.


import random

#a = [2, 3, 3, 1, 5, 2]
#a = [421, 81, 288, 154, 259, 217, 41, 461, 145, 217, 188, 208, 183, 314, 200, 265, 188, 345, 196, 372, 367, 313, 488, 356, 28, 277, 267, 119, 181, 497, 104, 119, 129, 120, 328, 487, 287, 318, 167, 491, 284, 476, 134, 181, 56, 49, 464, 109, 4, 343, 198, 313, 495, 345, 101, 474, 390, 5, 212, 351, 184, 187, 387, 334, 175, 458, 213, 28, 2, 203, 295, 117, 323, 25, 158, 234, 260, 422, 297, 148, 417, 351, 137, 63, 218, 278, 288, 199, 69, 262, 360, 384, 230, 240, 64, 198, 483, 105, 443, 18, 221, 118, 303, 195, 480, 58, 351, 445, 20, 261, 374, 393, 456, 186, 266, 205, 29, 184, 82, 111, 358, 154, 94, 106, 288, 152, 425, 99, 24, 166, 197, 273, 148, 79, 268, 302, 279, 57, 172, 361, 387, 264, 241, 422, 291, 147, 347, 374, 288, 157, 42, 455, 128, 257, 289, 293, 476, 449, 189, 190, 34, 129, 493, 304, 361, 94, 76, 59, 272, 500, 67, 213, 218, 67, 267, 153, 252, 164, 22, 415, 323, 58, 260, 120, 270, 185, 287, 341, 129, 338, 442, 148, 93, 114, 360, 116, 414, 361, 165, 150, 292, 69, 345, 308, 428, 35, 430, 227, 480, 7, 195, 119, 51, 181, 131, 295, 113, 209, 21, 286, 175, 249, 120, 212, 429, 252, 375, 41, 86, 379, 202, 157, 124, 65, 298, 304, 46, 338, 211, 316, 418, 461, 200, 164, 263, 175, 347, 84, 157, 377, 173, 14, 23, 57, 388, 113, 332, 400, 163, 493, 467, 469, 91, 388, 172, 369, 464, 122, 96, 220, 20, 116, 139, 435, 409, 91, 435, 334, 109, 198, 390, 133, 150, 268, 255, 272, 143, 218, 431, 104, 13, 443, 284, 341, 285, 397, 324, 80, 385, 488, 42, 10, 96, 443, 273, 213, 396, 207, 394, 131, 35, 252, 36, 61, 79, 371, 123, 201, 339, 409, 402, 437, 13, 481, 180, 205, 378, 128, 456, 377, 279, 408, 277, 431, 154, 394, 345, 60, 205, 181, 184, 121, 204, 418, 94, 14, 238, 66, 440, 415, 416, 481, 98, 223, 357, 422, 330, 430, 180, 214, 367, 131, 53, 325, 398, 428, 91, 418, 153, 70, 427, 475, 437, 65, 426, 101, 459, 250, 49, 47, 66, 233, 114, 70, 298, 366, 307, 77, 395, 197, 419, 149, 492, 268, 493, 476, 102, 129, 321, 103, 102, 139, 431, 468, 317, 38, 282, 419, 166, 187, 461, 352, 350, 102, 422, 319, 423, 9, 76, 416, 133, 341, 3, 406, 259, 323, 347, 245, 70, 33, 262, 313, 219, 426, 494, 345, 188, 8, 337, 81, 52, 147, 253, 131, 192, 414, 474, 341, 302, 441, 220, 408, 157, 88, 115, 458, 132, 482, 91, 251, 411, 32, 399, 325, 240, 448, 226, 330, 43, 30, 109, 411, 151, 224, 113, 306, 294, 95, 315, 247, 445, 298, 217, 177, 366, 7, 250, 273, 82, 355, 100, 468, 440, 415, 465, 147, 443, 361, 138, 204]
#a = [2, 22, 25, 16, 3, 12, 3, 10, 12, 8, 21, 1, 12, 23, 18, 4, 12, 1, 18, 16, 24, 7, 21, 22, 2]
#a = [2, 4, 3, 5, 1]
#a = [1]
#a = [2, 2]
#a = [2, 1]
#a = [2, 1, 3]
#a = [2, 3, 3]
#a = [3, 3, 3]
#a = [8, 4, 6, 2, 6, 4, 7, 9, 5, 8]
#a = [10, 6, 8, 4, 9, 1, 7, 2, 5, 3]
#a = [1, 1, 2, 2, 1]
a = [25291, 10593, 48905, 90778, 4254, 92081, 90295, 62807, 1401, 17648, 30571, 66118, 53112, 21466, 89448, 17461, 52847, 99967, 70798, 54129, 10106, 12232, 3698, 40866, 15416, 76417, 49220, 37995, 76421, 23201, 35012, 28694, 44452, 11612, 56462, 89627, 55753, 10883, 87164, 5109, 49539, 11221, 31154, 73923, 56136, 88884, 20582, 23415, 45418, 5277, 76998, 13142, 99679, 22479, 80357, 79400, 48266, 34425, 8849, 18121, 39527, 82196, 5701, 34669, 70192, 31285, 63397, 81859, 65597, 95162, 5302, 95734, 57966, 24770, 40756, 49174, 93466, 42185, 92916, 43218, 6106, 30477, 34392, 5640, 40991, 42265, 69288, 7675, 6398, 41257, 36760, 18042, 71069, 78580, 75962, 55270, 51194, 83611, 57136, 85724, 53904, 35471, 38943, 75625, 96087, 90032, 11455, 13421, 50566, 92303, 40906, 37532, 79606, 67751, 99086, 74496, 19997, 59534, 5502, 30058, 8323, 18395, 17830, 24180, 39253, 94225, 72842, 88428, 94405, 61876, 59066, 36540, 99507, 20711, 52486, 11549, 12662, 52297, 68047, 19876, 76165, 58657, 75894, 95707, 63005, 40552, 28117, 46782, 5161, 53439, 58377, 61649, 60235, 85025, 12649, 18580, 45270, 67978, 1092, 7648, 79256, 32226, 1359, 36422, 92812, 20346, 90023, 50381, 31073, 61995, 18636, 65150, 95421, 47173, 55754, 35369, 20633, 36601, 33515, 79999, 72162, 48846, 43190, 99669, 78735, 47751, 13265, 3487, 83423, 56110, 71768, 21939, 97546, 96055, 91980, 80310, 82113, 77303, 82067, 65073, 83955, 71805, 69166, 17828, 9135, 88898, 89462, 13959, 32759, 38091, 61630, 87830, 48898, 87700, 50918, 79767, 25869, 16534, 39090, 89002, 19855, 4782, 97322, 65737, 48741, 71104, 33797, 95708, 69152, 42304, 23062, 23681, 43355, 19071, 9988, 84462, 48088, 42751, 91324, 33067, 92362, 78067, 88000, 87901, 26532, 96844, 2032, 64438, 55805, 40886, 5297, 1485, 50974, 30798, 39406, 43476, 82505, 77230, 34247, 98832, 45308, 12300, 88155, 31251, 12690, 32111, 68989, 39522, 29174, 71925, 35906, 35753, 53624, 33885, 64607, 85594, 59732, 25519, 50094, 87115, 73041, 86216, 89414, 14766, 30685, 56466, 86635, 67455, 26940, 74534, 65677, 2691, 754, 80109, 29073, 30163, 30046, 29719, 16878, 49158, 93121, 93232, 59998, 87125, 8504, 50750, 21025, 14985, 9499, 82455, 66233, 21301, 46892, 49826, 72154, 42218, 36137, 81350, 9204, 59262, 41079, 27022, 86861, 42318, 10099, 75601, 9345, 33543, 20559, 89926, 13938, 33071, 77550, 59107, 51829, 55269, 87762, 56659, 91768, 97627, 58086, 69010, 48363, 22926, 46979, 4286, 22458, 23675, 89224, 63082, 92891, 6170, 77705, 40173, 31446, 89463, 4733, 72253, 98206, 17609, 76174, 62665, 89930, 81060, 35351, 86343, 94873, 14856, 4585, 54922, 71902, 53598, 6406, 96029, 66452, 21096, 81304, 69162, 65868, 57146, 3098, 64788, 9090, 90258, 62022, 6922, 92621, 85235, 18879, 85909, 6932, 73380, 65397, 97148, 93626, 69064, 31167, 3310, 93129, 89725, 96722, 36781, 21935, 96772, 63444, 73813, 17457, 96859, 12103, 27618, 25966, 2192, 59250, 17498, 83113, 95927, 58418, 92438, 49218, 87121, 92464, 2449, 79613, 74064, 56530, 83331, 21491, 53675, 25789, 79107, 27689, 37286, 58921, 10394, 36938, 25179, 38344, 44169, 88628, 20693, 54165, 37313, 77817, 76110, 41063, 3481, 51871, 14264, 23644, 27049, 34284, 2206, 15291, 10628, 3338, 36643, 99044, 98540, 30063, 72196, 19449, 20965, 51000, 65906, 68392, 21214, 46176, 39163, 14815, 11776, 22314, 68637, 56410, 83353, 27548, 53157, 30065, 30764, 97362, 94672, 8140, 55174, 81436, 47432, 69238, 42479, 57869, 20545, 3457, 24331, 82658, 80232, 38928, 43861, 11035, 85927, 32450, 91851, 35958, 96195, 26811, 64378, 77813, 15362, 75505, 31472, 40235, 25370, 71943, 14688, 72498, 17473, 63110, 48316, 47045, 87035, 70551, 72285, 94021, 27308, 88630, 15223, 87710, 84967, 25039, 88938, 89123, 73050, 36530, 41279, 9897, 93446, 2863, 5755, 22266, 84225, 34649, 41624, 25162, 58605, 3551, 6487, 20174, 16564, 74742, 99527, 70870, 22214, 88495, 54035, 34421, 73180, 53663, 39150, 12838, 34819, 22854, 39962, 95792, 88492, 14258, 22671, 23447, 65107, 75636, 52931, 36589, 13436, 13851, 68617, 61839, 41609, 60840, 20943, 60757, 38645, 50811, 32395, 6077, 81915, 27111, 93943, 95033, 32435, 71479, 1649, 57004, 70997, 4997, 6594, 81560, 5704, 89367, 68444, 48915, 90564, 54393, 97026, 38498, 12563, 42641, 96974, 35694, 1872, 57902, 98393, 30025, 49944, 46674, 95017, 88868, 81949, 93130, 57272, 91813, 59443, 57167, 54935, 86278, 29825, 62621, 15051, 15945, 30015, 60346, 19470, 96099, 54112, 37278, 4675, 43820, 99121, 10280, 971, 57414, 79858, 81004, 31266, 27964, 85950, 92049, 5872, 38071, 94104, 36979, 66592, 23195, 97381, 23998, 88098, 83911, 26777, 22771, 28408, 15289, 99603, 91805, 7242, 71176, 55040, 80161, 39857, 1669, 3478, 69638, 33616, 12220, 28859, 36085, 8465, 12419, 76965, 76640, 13694, 93284, 22433, 69382, 50686, 63051, 48877, 86064, 8679, 68560, 92756, 2204, 76320, 70461, 27588, 481, 95122, 6636, 10288, 2582, 69731, 62049, 12630, 26380, 22031, 27604, 71726, 78665, 16210, 76256, 34815, 6988, 46082, 84776, 36689, 90715, 71038, 5637, 88058, 15754, 41410, 90304, 11090, 95621, 58589, 85301, 32209, 59602, 3172, 85532, 77035, 23277, 80541, 72810, 44937, 16000, 99653, 48800, 61546, 15296, 5480, 44945, 99434, 26803, 19777, 36356, 64691, 74488, 35109, 50297, 81939, 31675, 3099, 82956, 30231, 90065, 13165, 82532, 3126, 93082, 69138, 54318, 56498, 84413, 49481, 8179, 24538, 40185, 97086, 72110, 80891, 8097, 25123, 88846, 31872, 24966, 22681, 25654, 29581, 19399, 70442, 77738, 14551, 22965, 28272, 86742, 31920, 24304, 83782, 71350, 93064, 83186, 65471, 91277, 31047, 7680, 47735, 85637, 59114, 16568, 53398, 53314, 51715, 10689, 68012, 51569, 41586, 75473, 19849, 3160, 23246, 63616, 31639, 47439, 73980, 89063, 71046, 27190, 28550, 66384, 32623, 50316, 9949, 70294, 30371, 61533, 83502, 66657, 5914, 3915, 42843, 2421, 66480, 14228, 47142, 60012, 51662, 71903, 60788, 16498, 60536, 57898, 94734, 97491, 560, 2772, 89925, 28416, 28095, 9627, 75747, 52754, 72014, 33288, 22631, 31753, 13576, 48686, 12955, 66765, 21742, 26207, 76762, 23925, 49751, 28293, 4435, 37462, 50984, 58218, 39519, 12080, 1519, 32921, 14232, 70574, 87642, 44897, 50333, 77628, 87981, 43259, 61574, 2632, 91903, 82549, 26798, 58862, 57990, 39375, 49268, 61171, 89178, 22649, 71093, 6632, 36773, 41517, 95452, 21106, 92815, 48853, 49782, 38648, 93316, 25864, 44089, 99000, 75521, 35141, 11014, 10184, 55880, 94316, 66016, 84649, 19349, 92201, 49779, 11511, 71208, 80317, 78392, 83425, 60519, 18615, 7571, 83781, 65451, 28315, 80875, 60604, 44002, 9850, 71740, 66193, 69947, 86972, 26578, 64056, 39604, 34165, 17056, 73621, 35837, 33367, 40370, 63912, 77973, 82275, 93864, 57841, 15880, 30352, 20388, 41198, 83975, 71530, 61026, 67941, 84607, 20228, 85976, 30673, 13123, 68142, 1673, 52582, 99038, 83083, 84213, 3876, 1405, 65235, 22737, 13391, 76210, 33454, 67977, 92063, 95207, 94303, 45855, 88425, 58913, 98998, 58600, 90352, 89656, 24588, 11748, 91007, 6524, 3506, 74396, 46566, 24546, 36834, 8765, 12414, 5665, 66717, 18282, 89003, 30273, 75941, 39004, 9416, 73967, 48009, 31998, 94415, 49223, 73837, 56562, 80746, 7791, 11540, 5236, 66970, 64683, 16952, 80855, 34794, 27904, 30814, 57047, 10858, 43616, 741, 65772, 29813, 12879, 1783, 91235, 85911, 46473, 39269, 68079, 29297, 4039, 96600, 50720, 54192, 17895, 12874, 36028, 19371, 29812, 52929, 95956, 54191, 29302, 24503, 14618, 27545, 21947, 11181, 29206, 40229, 88581, 23832, 29646, 82031, 60401, 73071, 14326, 9775, 45663, 86308, 88032, 94537, 52395, 36619, 41078, 85859, 26074, 64703, 84885, 48468, 74581, 81122, 34575, 85203, 66242, 36551, 39328, 67641, 16838, 166, 90224, 91259, 39172, 76397, 53687, 8477, 69701, 48087, 87687, 85579, 21773, 55421, 21759, 6888, 42196, 97982, 683, 45590, 96687, 91720, 44974, 91448, 11574, 61891, 55072, 56900, 21280, 51265, 98008, 72808, 19134, 35456, 46360, 78691, 43633, 23981, 74495, 59335, 9827, 57083, 58346, 5792, 53242, 73154, 78133, 28216, 52176, 35264, 37791, 28163, 29170, 15697, 65619, 98166, 7074, 87908, 33455, 25408, 53508, 53962, 95568, 96064, 23725, 31681, 55048, 52933, 95682, 38557, 79850, 22752, 28247, 15076, 31665, 2068, 46537, 94188, 23921, 83044, 78918, 98509, 12696, 71323, 45259, 4597, 89524, 2560, 57439, 19506, 96412, 16824, 74095, 66573, 18930, 57733, 92292, 22992, 48867, 43718, 90994, 74151, 47387, 25032, 9387, 45749, 11381, 88588, 67604, 43743, 4917, 42574, 26198, 22238, 97210, 78305, 72809, 75326, 69209, 15611, 85975, 21154, 74767, 13668, 22182, 45343, 81016, 63242, 24249, 72198, 9600, 67309, 7866, 32347, 94869, 50382, 85995, 3852, 1832, 4027, 46941, 73814, 95460, 3895, 88339, 96668, 51559, 33961, 73584, 72853, 26810, 71233, 49668, 96850, 96994, 94579, 94414, 38924, 88497, 72197, 7037, 53215, 92272, 11380, 26359, 7999, 71410, 53971, 12784, 32923, 34286, 23683, 67743, 80470, 34610, 65854, 70727, 25082, 97395, 77807, 28403, 41116, 57478, 76522, 65680, 9561, 7220, 37568, 61500, 99767, 84477, 53566, 68631, 70191, 9524, 96021, 62025, 38157, 13379, 31456, 86749, 85767, 31347, 73084, 91297, 95386, 18279, 80485, 12147, 29741, 65903, 81101, 49385, 10410, 46604, 67509, 79957, 65385, 27453, 25747, 94240, 53336, 66015, 88808, 26589, 9706, 56613, 86435, 71449, 5901, 56096, 54695, 28815, 44067, 9354, 57388, 88528, 51084, 32075, 63737, 42612, 79117, 80496, 96292, 54728, 72094, 69348, 96015, 23763, 19524, 21675, 83433, 65488, 65185, 83559, 86024, 88028, 51850, 67530, 29587, 80814, 55548, 33422, 67737, 83880, 84840, 93114, 70112, 76413, 22215, 80585, 13795, 67414, 52590, 4397, 80663, 32620, 59271, 22491, 57919, 98689, 67749, 31693, 66873, 13004, 35406, 78792, 67642, 74845, 21257, 31514, 2963, 6973, 84719, 45532, 17139, 251, 53228, 85445, 7803, 62520, 42284, 42531, 10337, 97597, 3703, 33941, 279, 68017, 18866, 45506, 75339, 33950, 30688, 33810, 68399, 90419, 17091, 61415, 59741, 96649, 20915, 38849, 7960, 7608, 68974, 55336, 21824, 17805, 16155, 14195, 76563, 8000, 73413, 23232, 97068, 47226, 84365, 70754, 12598, 65623, 58409, 86638, 75390, 65996, 58619, 38162, 27976, 5093, 83144, 21074, 63606, 46538, 2476, 68613, 73826, 36229, 3820, 45228, 45772, 57066, 97650, 24856, 83943, 98702, 65977, 89811, 14263, 723, 99513, 71921, 20178, 96200, 6315, 53258, 89574, 23896, 94353, 39429, 67404, 8198, 75253, 69114, 346, 6525, 58966, 43584, 54818, 4481, 4970, 7246, 55797, 88496, 47519, 85114, 78592, 72186, 73447, 770, 7163, 40142, 12101, 12482, 23599, 50425, 89530, 76487, 67183, 92393, 14319, 17334, 95590, 69881, 15115, 92252, 47128, 86968, 3993, 71993, 77302, 60997, 17012, 19107, 80789, 59888, 39112, 59619, 52192, 26029, 68545, 44691, 5258, 60632, 13060, 39895, 97957, 44041, 18787, 98269, 78930, 11867, 97434, 44424, 96169, 70063, 89447, 63362, 84728, 41827, 27626, 9001, 27603, 86217, 29661, 36363, 29763, 19963, 63141, 14669, 11479, 94009, 46158, 12613, 44105, 31657, 44807, 42665, 15690, 9940, 85762, 73993, 39724, 53727, 40561, 5867, 70780, 14024, 68542, 73152, 93191, 19561, 19049, 98197, 2209, 60822, 60449, 7140, 57435, 12599, 1285, 76819, 83008, 88999, 13687, 86974, 54229, 18037, 7091, 13691, 60719, 3034, 53520, 56931, 90721, 70243, 3014, 81822, 54186, 51006, 70134, 71877, 74378, 39106, 19894, 2393, 53424, 88399, 26046, 87674, 90856, 68350, 44269, 76982, 59800, 78378, 53384, 67973, 34092, 28665, 423, 88666, 85467, 55500, 67243, 5570, 52301, 93076, 34662, 37944, 59073, 56614, 71029, 55135, 97655, 82, 5614, 65455, 79974, 21513, 37468, 53893, 39058, 63329, 73016, 49356, 10691, 92235, 38097, 63859, 89167, 97855, 88212, 96167, 67337, 67484, 75615, 28012, 13890, 2525, 15569, 6253, 64646, 38061, 69873, 28774, 25478, 92295, 72496, 29326, 75514, 52962, 30417, 46777, 10054, 87723, 14549, 15064, 11870, 61223, 62038, 57749, 76878, 78084, 8754, 41403, 81448, 37825, 52822, 43163, 42828, 46087, 58223, 88847, 95746, 81152, 79244, 46866, 55422, 3257, 78473, 72559, 1101, 16064, 52690, 52355, 18775, 40645, 60157, 37917, 50281, 7964, 80306, 17761, 15488, 79773, 59771, 3779, 43492, 14671, 27572, 68148, 25697, 68547, 57021, 78484, 93871, 92907, 4205, 28612, 23215, 80879, 6489, 12185, 20905, 71440, 80868, 96713, 40496, 74231, 63197, 54876, 60670, 22452, 16599, 62353, 11171, 36227, 66730, 79266, 60514, 42694, 73871, 71122, 8359, 50170, 12576, 85433, 976, 4488, 82884, 77066, 95071, 18382, 80588, 40506, 89643, 99420, 64099, 68882, 89453, 48752, 26155, 88954, 84130, 85378, 75842, 76103, 86716, 20454, 72052, 18781, 15171, 28609, 38814, 88367, 5191, 14652, 56148, 12853, 10402, 67647, 30693, 38973, 48513, 17017, 82384, 9538, 94352, 82706, 14031, 17417, 51477, 3120, 35398, 53920, 57904, 12369, 93671, 98763, 81921, 54084, 70398, 95397, 76929, 49593, 29374, 19283, 57271, 50639, 49452, 16243, 3278, 29173, 56709, 52264, 45916, 57415, 71273, 22507, 78637, 67126, 50671, 61637, 82321, 62141, 31082, 97647, 42193, 56782, 32774, 83858, 80850, 34517, 35175, 22302, 97074, 84690, 8175, 57485, 2273, 62719, 62040, 31170, 74774, 3404, 95804, 45330, 58012, 32843, 33122, 27650, 8436, 71684, 89781, 47745, 56480, 42097, 67733, 4535, 86759, 38040, 64284, 96692, 59274, 78821, 69619, 70522, 25640, 74464, 56308, 25214, 71997, 32416, 45150, 16941, 93017, 67557, 14578, 58545, 94870, 58034, 44136, 87835, 30954, 4916, 31110, 24883, 59846, 87333, 8506, 60324, 78335, 60201, 34594, 45471, 92686, 79750, 36014, 3187, 67767, 57794, 46484, 36173, 46868, 69032, 3527, 334, 34167, 24969, 2765, 50565, 65645, 35123, 48527, 32533, 90288, 76074, 92192, 43916, 27171, 46764, 63888, 92133, 34223, 18442, 4447, 79718, 50570, 17469, 14125, 91677, 10892, 36282, 93400, 21471, 16551, 31642, 89209, 13277, 82355, 66271, 8047, 71865, 3606, 34680, 28660, 5918, 73782, 4988, 5127, 25239, 42415, 76718, 52809, 10602, 19250, 21564, 7057, 69923, 97722, 25382, 8971, 69268, 17353, 46532, 68724, 83306, 10705, 30508, 52359, 59008, 83182, 58174, 15135, 14807, 98835, 13812, 35814, 25034, 69665, 38751, 63140, 45110, 19584, 16435, 88777, 38325, 88312, 80921, 77364, 7607, 9457, 58562, 92034, 26818, 87027, 95819, 31496, 81028, 69984, 29909, 83097, 45443, 78983, 83443, 74007, 47239, 54341, 62636, 57544, 14568, 71275, 90363, 64780, 75149, 51825, 85013, 87691, 56314, 96061, 29629, 63488, 8212, 6091, 88302, 50497, 23394, 51580, 90983, 14345, 87180, 5436, 29255, 33538, 13705, 65297, 78903, 47874, 98139, 33666, 19053, 42610, 97643, 994, 98443, 67450, 86973, 23601, 58390, 29976, 30725, 1874, 30078, 84046, 78680, 88909, 73372, 13549, 69302, 18144, 6126, 85105, 33663, 51293, 96215, 82304, 96841, 98004, 36832, 62391, 17438, 22331, 51838, 28388, 52759, 29705, 2347, 11585, 49245, 43072, 63695, 82092, 2335, 51444, 40315, 12331, 86297, 99862, 84685, 60407, 52119, 17504, 74390, 53011, 12095, 17189, 99948, 11253, 38801, 57236, 53140, 4557, 69548, 54590, 42440, 94495, 77405, 38341, 96580, 35675, 4851, 94650, 19622, 87618, 62817, 37158, 46005, 24511, 33576, 28589, 8213, 93128, 77443, 6242, 92831, 92928, 90652, 20262, 40773, 75052, 96226, 62599, 98099, 14934, 55361, 3590, 12290, 95979, 98158, 14434, 50053, 45611, 9281, 38337, 42948, 14204, 33266, 52593, 91172, 85568, 38002, 6679, 97905, 12376, 28671, 5401, 36369, 68354, 44289, 13129, 86956, 74360, 49787, 65520, 64613, 44260, 48119, 91250, 28434, 35654, 5021, 33022, 45621, 23648, 59746, 86337, 7681, 86326, 30629, 17763, 20459, 42287, 5968, 77951, 49375, 60539, 76482, 73272, 95558, 72114, 22881, 81539, 69847, 41213, 35910, 5924, 46110, 13062, 49345, 80823, 59910, 48245, 63346, 45960, 99953, 26829, 39291, 18590, 25877, 43982, 56956, 54624, 56297, 45271, 38510, 56998, 25182, 80960, 70935, 94981, 70817, 3995, 27775, 47420, 62536, 14337, 24859, 70877, 76649, 97402, 34423, 38239, 80611, 48667, 59839, 34974, 70071, 6723, 2473, 92537, 41900, 10058, 7193, 46607, 84333, 80390, 80217, 90012, 10537, 94937, 50598, 20571, 23930, 50825, 41021, 81326, 28845, 37920, 20133, 8202, 72532, 7567, 59077, 52351, 64485, 47891, 79128, 82961, 2178, 89427, 42001, 47485, 16923, 84938, 63929, 49127, 54518, 85307, 61035, 94915, 55912, 99219, 39788, 7575, 17430, 50705, 31788, 22685, 83042, 7030, 53461, 62541, 1974, 80599, 17069, 16897, 34966, 30545, 61001, 6835, 16917, 15243, 46733, 66511, 28178, 69141, 94880, 71036, 12515, 79770, 5040, 56646, 49773, 79200, 45649, 64668, 78674, 65186, 83438, 39613, 73383, 76724, 66532, 44133, 87503, 66693, 86479, 36533, 16810, 45149, 19621, 33613, 61632, 51691, 71514, 87766, 12667, 71898, 63464, 48026, 35880, 25024, 10196, 77360, 16679, 79265, 28733, 70889, 33, 95415, 31988, 48929, 84063, 77277, 31314, 94843, 6547, 26911, 3943, 57403, 78602, 90247, 77312, 13440, 44652, 81322, 25854, 56442, 73193, 38204, 81578, 81487, 92131, 18851, 45865, 85574, 76176, 66165, 41614, 50489, 82219, 5965, 38043, 51100, 5402, 93804, 79417, 94994, 5915, 15515, 35461, 17668, 96401, 93531, 17873, 29903, 65254, 53445, 64440, 15110, 69769, 47969, 35889, 85529, 51484, 95818, 64871, 22648, 11805, 38655, 31123, 13722, 77416, 86677, 59441, 79, 77783, 75418, 8638, 38824, 76947, 72520, 49365, 65845, 33706, 81270, 53571, 83834, 810, 53418, 49190, 96585, 72503, 65004, 14974, 87037, 86361, 71445, 60289, 60814, 67332, 1992, 7007, 26053, 62826, 39500, 62482, 50931, 82442, 91364, 57448, 52169, 43886, 71447, 27167, 55635, 66543, 11946, 35464, 88286, 15265, 63350, 78713, 26843, 51626, 63736, 78243, 43093, 17641, 871, 83513, 25207, 57767, 65436, 7004, 79227, 77318, 57377, 34059, 35327, 76976, 6418, 86694, 83706, 32029, 35244, 6930, 54531, 56642, 42213, 6175, 50261, 12102, 2508, 83891, 75095, 71213, 8410, 75774, 28776, 92555, 21882, 66408, 61262, 63226, 29428, 91552, 18963, 81575, 3253, 73062, 95878, 39073, 28790, 79109, 92933, 11132, 88856, 31620, 87118, 86800, 99818, 57610, 26317, 6819, 62335, 79113, 71416, 65300, 34675, 65966, 23351, 14000, 78239, 99905, 67150, 95388, 15859, 65129, 7869, 44435, 94587, 21541, 50190, 85208, 92552, 56040, 65646, 93631, 57151, 68528, 43243, 77473, 19117, 93814, 47819, 36670, 90182, 69295, 80932, 39689, 13064, 15230, 89249, 81920, 88860, 41626, 56285, 52343, 57264, 26076, 88843, 81037, 70271, 40149, 60558, 9947, 71918, 45042, 24427, 57394, 17206, 91742, 8720, 30014, 93189, 59485, 6680, 52539, 74529, 33202, 98659, 32180, 26661, 70036, 44344, 24664, 79966, 19945, 56144, 62009, 81975, 90717, 67341, 44886, 98451, 19362, 56619, 59597, 56873, 28313, 85865, 5974, 9788, 51255, 42135, 8564, 50717, 86489, 27678, 63862, 32813, 84542, 27278, 84423, 2636, 76662, 16315, 92132, 69093, 3458, 90974, 88883, 59520, 9423, 87469, 59484, 84777, 67552, 85779, 84859, 60040, 17045, 49021, 57329, 19511, 11305, 63036, 3068, 30452, 66690, 48418, 92903, 74106, 15658, 5042, 32619, 47750, 38633, 91417, 9116, 59198, 45543, 40873, 58210, 32040, 70840, 37077, 67272, 9043, 65467, 20479, 35248, 57154, 3009, 90648, 83607, 20882, 4234, 89964, 55044, 35164, 64634, 15731, 97420, 64073, 34985, 59821, 71482, 12701, 26004, 90, 36797, 40790, 32849, 7264, 67390, 10386, 2235, 89206, 77128, 2126, 97515, 15962, 56414, 60209, 85404, 64506, 70578, 67791, 60652, 57731, 49721, 28873, 98584, 20950, 5599, 35384, 88510, 61440, 22873, 62114, 47832, 10463, 55896, 65033, 79720, 84962, 9273, 18398, 26396, 15427, 70184, 7231, 97015, 82052, 92666, 38596, 35511, 23341, 80113, 40900, 75664, 53530, 67241, 18074, 339, 74011, 78895, 72928, 9333, 19282, 53471, 74606, 43415, 68975, 54971, 17247, 50443, 70096, 64564, 54435, 22747, 37026, 96364, 68527, 93901, 62982, 7033, 93344, 41784, 49659, 85240, 92725, 41325, 71784, 83021, 5927, 66986, 21249, 69451, 25701, 1486, 17132, 22128, 16659, 19787, 77556, 93811, 61481, 63142, 17720, 15420, 82169, 20176, 21079, 59995, 33590, 18179, 59407, 90469, 46388, 83164, 89341, 84185, 96492, 74458, 74404, 9436, 18047, 55906, 60155, 8873, 76941, 21312, 78913, 39902, 84192, 94979, 88772, 70475, 54219, 56259, 63600, 14708, 60354, 49941, 54960, 61871, 1042, 95370, 18721, 51857, 47981, 46768, 92723, 16523, 32840, 65838, 59312, 92865, 52936, 4436, 50086, 3199, 10067, 54889, 25555, 68923, 89828, 44442, 64195, 70617, 71209, 64765, 75183, 98192, 13912, 21250, 65013, 15085, 55954, 42834, 44905, 4862, 34054, 88341, 18408, 31057, 28766, 96452, 78266, 25466, 75218, 7710, 97336, 35473, 92914, 94825, 55345, 95339, 98311, 37099, 95504, 26203, 5310, 16490, 65294, 81325, 71004, 62373, 75213, 63355, 17923, 37768, 66578, 37930, 54195, 88203, 35111, 11610, 72914, 32763, 39635, 8133, 33346, 45283, 99476, 56183, 7456, 8906, 36040, 15023, 48534, 61482, 24949, 69596, 1228, 70896, 32608, 69300, 74654, 97189, 60108, 76040, 72617, 55411, 70000, 33932, 56980, 48745, 22134, 1597, 6870, 91009, 82127, 69203, 84095, 56661, 73620, 16326, 51553, 95922, 12422, 9122, 36025, 62688, 98755, 27393, 88102, 33536, 76669, 54481, 65729, 3637, 82182, 93149, 97202, 26561, 2430, 26825, 53699, 45315, 61057, 91999, 49404, 18647, 46642, 74393, 5473, 6140, 27994, 51891, 1483, 65193, 99183, 50337, 2381, 69261, 17331, 87137, 44921, 69487, 2009, 5940, 52505, 63080, 78097, 55185, 56655, 89077, 93440, 52681, 38566, 67106, 92328, 25623, 61844, 58107, 93930, 62869, 59552, 32376, 15994, 93604, 6061, 42290, 15798, 7036, 59913, 75861, 1300, 64719, 30334, 88436, 1741, 40631, 63712, 9703, 37671, 74576, 11115, 23160, 57769, 15633, 49044, 95380, 28980, 83881, 9513, 58431, 57092, 54280, 59914, 95354, 85616, 60586, 65128, 37060, 52253, 14615, 19181, 42483, 44681, 21864, 77596, 13332, 63011, 65628, 93913, 9543, 66391, 96494, 13545, 33362, 17275, 86875, 56472, 91247, 76479, 21959, 15554, 61628, 48477, 47332, 34471, 78039, 57055, 69470, 69995, 39821, 3699, 50064, 85415, 1809, 78315, 35674, 39461, 86580, 90170, 63669, 25476, 98912, 88091, 42799, 29472, 51114, 79293, 95196, 26969, 41949, 67654, 8368, 77372, 9209, 8561, 42796, 226, 8592, 488, 5524, 24006, 20478, 20116, 33466, 66553, 49462, 47876, 73488, 29492, 89786, 36196, 86038, 68671, 50476, 34870, 33989, 7507, 19409, 21937, 59729, 29332, 27925, 64643, 70267, 28090, 99261, 69786, 14129, 57976, 73654, 18051, 85144, 11702, 27070, 90933, 31829, 3194, 66957, 53810, 86644, 25387, 55177, 38979, 19452, 12174, 28431, 57063, 93579, 39717, 59785, 91827, 33888, 35897, 69805, 91612, 44698, 95063, 45579, 43825, 74087, 91497, 25050, 29129, 94936, 42331, 23313, 42577, 2134, 39977, 8307, 46534, 1408, 34445, 72969, 86670, 83828, 62469, 30517, 39425, 57850, 38469, 14436, 73943, 58453, 22007, 38823, 76706, 47122, 44526, 1004, 34504, 573, 4158, 94910, 23710, 11414, 62229, 36983, 27535, 68677, 74033, 56847, 93809, 88508, 13800, 28812, 58557, 61441, 39744, 46370, 37014, 14814, 83266, 3321, 74164, 12075, 92638, 84454, 15343, 53771, 1031, 24490, 42396, 56397, 14717, 43707, 91886, 34039, 11994, 37109, 12921, 71294, 19354, 50481, 3923, 83697, 24687, 92844, 24461, 80857, 69969, 91361, 75195, 63307, 11635, 42855, 10615, 1489, 76489, 89771, 36161, 9404, 36030, 65534, 15977, 29684, 88929, 48217, 22393, 98016, 30, 6279, 25764, 81221, 18533, 5747, 86190, 85426, 87174, 41446, 17649, 56376, 33370, 72830, 3004, 17043, 75914, 26835, 61443, 11859, 18871, 19948, 3776, 89019, 3246, 13107, 7872, 39645, 57523, 50265, 47860, 58432, 60098, 84731, 15376, 23720, 70521, 58911, 22276, 29337, 87667, 30041, 20596, 20443, 26984, 29915, 47454, 69854, 24108, 20167, 51716, 32115, 65902, 96795, 83193, 4096, 8204, 2276, 90639, 44083, 84277, 97250, 5952, 66720, 49043, 47246, 71368, 7730, 11886, 10389, 79328, 19662, 46270, 56513, 70892, 17970, 69177, 57029, 65904, 71520, 55976, 11812, 84428, 71977, 65435, 37254, 69234, 20795, 21808, 81089, 50962, 11130, 77953, 14665, 57629, 96158, 45583, 72786, 99738, 16075, 90659, 96109, 82474, 10479, 1941, 86832, 59255, 76824, 77697, 46482, 62355, 86354, 38668, 40066, 6843, 27868, 18493, 51516, 80451, 68954, 99382, 55572, 85586, 17254, 38806, 66082, 8543, 69124, 570, 31546, 51433, 35610, 11011, 3148, 99320, 20157, 65261, 90435, 47955, 67094, 28423, 47741, 147, 30881, 28990, 91044, 60510, 17093, 97965, 97455, 94475, 18481, 99313, 71775, 65223, 73753, 26211, 50352, 43531, 81340, 62403, 72690, 55964, 7383, 92440, 39687, 62057, 28160, 22542, 38756, 79579, 67653, 45361, 40544, 73901, 17289, 54802, 73007, 58160, 70, 69058, 98899, 49690, 46378, 20939, 89352, 50149, 41162, 39736, 63958, 94960, 54848, 56742, 5699, 81834, 51385, 60188, 37482, 73756, 28617, 71148, 43818, 48889, 53588, 51951, 45519, 38186, 80862, 15484, 9876, 46332, 76224, 2400, 69481, 65821, 13530, 72963, 18679, 52932, 5319, 61305, 34353, 30018, 83709, 7351, 59581, 74299, 7658, 22198, 50802, 96023, 6766, 69556, 86906, 84954, 4607, 50005, 38673, 62263, 1793, 35390, 87147, 51427, 7065, 37233, 84000, 39839, 20455, 88139, 17024, 39919, 25157, 2253, 99209, 62723, 3413, 7393, 99696, 96207, 67590, 15165, 9590, 48763, 36341, 35919, 55335, 9939, 17919, 31363, 34584, 22357, 18295, 42446, 58225, 92370, 61790, 15942, 3988, 23777, 14804, 94180, 26703, 52111, 65604, 3911, 874, 95401, 18368, 27185, 63034, 13110, 41314, 57738, 86952, 50761, 77398, 25332, 42352, 52550, 66148, 4409, 64063, 12990, 79291, 43176, 92, 13970, 51550, 89033, 99591, 58588, 40710, 56943, 21100, 77797, 72688, 78352, 64275, 76741, 71007, 49417, 2642, 6199, 73994, 96747, 13514, 21566, 76383, 30843, 75186, 85113, 28578, 51487, 62139, 16929, 91142, 47006, 5091, 22186, 76090, 39840, 358, 11425, 73100, 84495, 40543, 9370, 82281, 34615, 71199, 81689, 81476, 82864, 76845, 64739, 71049, 37969, 1656, 95059, 75791, 544, 85885, 9927, 58120, 56340, 85103, 23083, 36379, 7213, 87273, 3459, 23764, 51545, 2247, 43024, 55265, 35331, 87017, 79596, 10989, 14362, 51153, 44332, 90732, 22395, 70470, 27961, 59214, 25001, 82118, 79270, 89883, 54941, 46403, 98655, 11025, 67701, 60697, 60330, 74399, 17846, 34646, 45683, 89290, 78667, 15770, 38872, 91177, 35582, 13579, 37361, 9874, 72023, 78687, 34872, 2912, 40718, 13167, 88330, 73347, 10793, 47273, 85490, 34621, 29951, 12326, 82781, 67357, 94566, 80837, 4852, 18303, 99352, 77792, 59161, 39234, 8439, 49813, 98310, 91045, 88633, 43295, 55027, 51541, 35732, 82905, 1946, 51389, 67629, 21416, 76408, 6741, 78885, 60680, 87285, 52555, 4537, 35160, 56143, 4001, 25037, 62927, 83456, 34933, 61775, 73418, 7302, 61317, 68099, 94125, 84473, 36582, 90832, 30106, 62499, 99440, 38553, 1978, 99432, 21933, 70155, 31203, 92687, 86137, 28556, 39714, 29949, 40875, 48508, 95709, 69229, 31909, 12396, 20733, 66087, 37219, 92601, 60076, 83985, 96116, 19306, 66068, 15637, 49233, 77907, 1918, 28404, 13499, 56106, 78725, 64830, 29509, 88241, 20288, 72772, 16695, 53162, 51252, 13983, 17297, 65830, 59385, 4752, 34224, 91033, 79077, 94770, 53549, 20985, 73377, 1504, 91208, 54080, 9584, 4826, 72377, 28158, 69292, 69503, 34342, 26809, 87176, 39373, 65572, 63819, 61665, 8039, 86202, 37384, 77274, 63236, 40960, 60231, 24661, 48664, 32800, 63153, 59432, 34497, 59731, 21976, 73708, 93853, 84029, 21669, 54114, 7001, 43664, 93328, 93491, 33657, 35166, 37149, 19943, 71457, 8652, 50124, 66206, 6186, 55261, 50368, 97563, 63774, 65754, 43109, 32950, 5213, 72387, 20642, 27491, 25197, 57234, 7934, 24615, 77391, 86272, 77814, 78468, 65614, 56978, 99408, 70888, 40870, 97078, 24473, 74036, 94813, 98772, 73563, 68999, 65509, 64556, 84810, 77464, 83148, 33281, 74838, 60458, 24677, 65354, 37691, 32322, 75942, 81723, 71429, 10190, 46092, 58024, 60430, 6314, 6762, 19885, 82022, 46040, 55656, 46488, 22135, 74424, 27704, 27289, 3874, 32047, 60230, 52215, 19439, 90297, 33653, 96737, 42178, 73699, 70315, 19680, 73220, 43844, 42764, 43690, 84709, 44245, 87413, 2482, 65377, 21083, 69967, 51863, 89692, 55462, 31061, 84158, 61092, 33369, 39578, 26145, 5916, 74752, 46687, 13141, 39185, 22732, 88815, 27792, 32794, 94757, 96353, 11825, 59318, 61274, 41260, 52869, 90701, 48204, 92343, 93532, 65194, 73040, 27019, 48672, 36132, 22268, 17548, 88819, 65103, 58353, 48575, 69538, 96287, 55623, 99287, 7864, 32328, 70428, 81056, 56940, 87231, 55129, 16347, 73091, 81334, 94074, 56660, 86349, 47247, 9000, 99244, 62063, 7574, 56061, 1429, 58271, 6338, 77569, 28427, 76046, 50682, 78809, 44128, 36154, 4437, 53432, 20433, 86617, 32573, 79522, 74631, 1382, 23844, 60878, 87984, 24773, 60735, 2130, 82306, 11722, 8973, 78813, 95888, 84353, 61620, 44549, 87106, 78158, 70648, 76264, 59969, 66088, 38748, 45401, 60417, 54837, 26030, 76725, 40354, 62781, 29579, 17025, 5768, 4710, 89726, 25863, 41423, 43064, 49716, 69894, 37503, 19514, 34340, 15483, 17143, 95555, 37642, 787, 20623, 86425, 2316, 31594, 61923, 70284, 73137, 7725, 17506, 5797, 94176, 45903, 13365, 26691, 47055, 35684, 77603, 19838, 82429, 83506, 36680, 79616, 65431, 56145, 43754, 16633, 13253, 56504, 65539, 47831, 19206, 83340, 83893, 38584, 59920, 13508, 74611, 50246, 15219, 6002, 98695, 34979, 85495, 7316, 7107, 29606, 94539, 63049, 33482, 83876, 4263, 32927, 62793, 9547, 35203, 70288, 39199, 7386, 80054, 14038, 76730, 55057, 3906, 77656, 55143, 23097, 39777, 21444, 79366, 35235, 87584, 47636, 88504, 24653, 45837, 55148, 20405, 45452, 27580, 8759, 86159, 9367, 99160, 48830, 50508, 70923, 47049, 4773, 23797, 69534, 83024, 68449, 4494, 37598, 11650, 60460, 71512, 37564, 13366, 61283, 96901, 12230, 63572, 60263, 44277, 29922, 91778, 74912, 2741, 73301, 87456, 19447, 5953, 22021, 38827, 96117, 52257, 10673, 88253, 14360, 35571, 53871, 13173, 5517, 77686, 90518, 39593, 62047, 97583, 49854, 44505, 47928, 91647, 1421, 37848, 51166, 31922, 56512, 83276, 19487, 61956, 56539, 34771, 19463, 92227, 76055, 56052, 22093, 67830, 83139, 12916, 3261, 32268, 41300, 93956, 92776, 86225, 83700, 25822, 96174, 80727, 67601, 44860, 60069, 68729, 68516, 62197, 7440, 13756, 28973, 19877, 56844, 21709, 63723, 44927, 96269, 1606, 53846, 55558, 64403, 24288, 14813, 52808, 43152, 58865, 27799, 20290, 66341, 8320, 97917, 81194, 8154, 89724, 68257, 33857, 2809, 16255, 92289, 28582, 40451, 45885, 40319, 6044, 32078, 34215, 51064, 68288, 40517, 63401, 86022, 16007, 69337, 18386, 17622, 10922, 99788, 8769, 49419, 72189, 9408, 5248, 46188, 94751, 41291, 52552, 95378, 23541, 74318, 4491, 76682, 95052, 5028, 71074, 63462, 44611, 71515, 95243, 28385, 13311, 72706, 55378, 93905, 95414, 47659, 24634, 89330, 51172, 59740, 38250, 84530, 96403, 6023, 45535, 4147, 10039, 15732, 33509, 49491, 66131, 50367, 5853, 63608, 61152, 78019, 14772, 62513, 72087, 77207, 80040, 80436, 13750, 16692, 14299, 49227, 51138, 63156, 12219, 43180, 44803, 33416, 51091, 95310, 16284, 15077, 43563, 92584, 71279, 57547, 75498, 82786, 54638, 30570, 38122, 16196, 12107, 71597, 87612, 54867, 15998, 11893, 79813, 44679, 85189, 82325, 62546, 16948, 80528, 4540, 4861, 18502, 82696, 75617, 22351, 75751, 99122, 91977, 36053, 98433, 37087, 4721, 86819, 78381, 22708, 78956, 6935, 78824, 16685, 26702, 63037, 60464, 48584, 98735, 51527, 91509, 15865, 73721, 43975, 11991, 72945, 4070, 19316, 33212, 43833, 1257, 41669, 46743, 67966, 8363, 70697, 66075, 9002, 51420, 20645, 32727, 63750, 75512, 26431, 1180, 83332, 25124, 50202, 11762, 79604, 48488, 30516, 40448, 67974, 22897, 81262, 11537, 77683, 61627, 46506, 33410, 31440, 31737, 27808, 37786, 10577, 14994, 13285, 16588, 34752, 36451, 43767, 40702, 88350, 12041, 32542, 60941, 62406, 25106, 65481, 95840, 65541, 78620, 97397, 46463, 76212, 52657, 20024, 11001, 50234, 8734, 36826, 18447, 86218, 4610, 34418, 86540, 96799, 14909, 88947, 24638, 13706, 42893, 87918, 7385, 20709, 57599, 3252, 39400, 81806, 19542, 1999, 46684, 81217, 40107, 25235, 84286, 44528, 1766, 48554, 4712, 2847, 87507, 1889, 91876, 97450, 37769, 74515, 31304, 64320, 26567, 29425, 38870, 18858, 23838, 12930, 9467, 42789, 55934, 22183, 37520, 59669, 21529, 99700, 41502, 40424, 20701, 61851, 41207, 82612, 13054, 76009, 92899, 45635, 71168, 74034, 86332, 7055, 94370, 87556, 2966, 7757, 19042, 19639, 51384, 80965, 18528, 7627, 39334, 42934, 52436, 77079, 44950, 52372, 97886, 67612, 30827, 10079, 54373, 18863, 47851, 96565, 44184, 82059, 42281, 77570, 63932, 80574, 43572, 45608, 48887, 18453, 94431, 45355, 73376, 20640, 12439, 66009, 66680, 20946, 88578, 68876, 21215, 98080, 84612, 70458, 4170, 64447, 49505, 37127, 28185, 45776, 38616, 71358, 72942, 6294, 5756, 25437, 63235, 67906, 73927, 32940, 95197, 11712, 53671, 95942, 41154, 67564, 11571, 39371, 76626, 88984, 88266, 20258, 3832, 40137, 68981, 50390, 25584, 81641, 61125, 52546, 90962, 80409, 34995, 65905, 26548, 74692, 63682, 35097, 4549, 3786, 36140, 77858, 49819, 15973, 58579, 32736, 56402, 29923, 19861, 51085, 51445, 64829, 33685, 12134, 26776, 1183, 92983, 91464, 97298, 29118, 11955, 51695, 95854, 68363, 40808, 50909, 65506, 38726, 92074, 66516, 63045, 6523, 78476, 66611, 57777, 28365, 59542, 34428, 31862, 9517, 30471, 78900, 15489, 43539, 22175, 23910, 97589, 67079, 88826, 70394, 5580, 9609, 77998, 87603, 73094, 68552, 3871, 54639, 65788, 27173, 92288, 40933, 53474, 42509, 55829, 21033, 44276, 99165, 46551, 33324, 16423, 8247, 27386, 4140, 69659, 98339, 1804, 96393, 87523, 68135, 22081, 95842, 54141, 54415, 65284, 93911, 19538, 74031, 307, 39289, 2440, 37777, 8641, 98391, 41171, 63813, 59337, 16733, 4583, 29724, 76597, 49416, 40071, 23076, 95053, 81745, 95488, 13293, 14294, 4338, 42510, 4114, 5369, 70103, 7955, 25802, 16275, 53151, 80487, 40901, 53229, 25765, 42657, 54447, 15956, 64814, 61089, 46901, 95597, 85138, 45756, 92400, 71013, 23719, 23974, 49924, 8990, 75999, 58397, 34308, 7924, 48369, 72495, 26407, 70021, 65542, 33463, 57747, 50706, 56044, 42176, 44732, 25429, 29360, 87113, 66285, 40982, 92655, 26855, 85557, 88429, 22517, 76655, 88229, 37134, 74116, 90565, 76749, 86880, 33935, 67348, 72771, 96672, 34666, 60926, 71461, 69362, 25572, 50929, 4201, 60614, 44262, 76201, 6171, 74241, 24313, 33267, 10037, 34667, 79069, 60067, 70995, 37622, 11397, 6339, 74270, 66411, 45975, 43001, 53082, 25936, 20426, 78990, 10075, 98515, 80555, 71010, 37018, 86431, 56901, 7702, 66438, 38873, 83012, 5066, 22260, 71712, 96, 63341, 31883, 88168, 36545, 67837, 19167, 61557, 42563, 17537, 52214, 64595, 9872, 23416, 5468, 57979, 5850, 58885, 32691, 46986, 9573, 60179, 72806, 92286, 48448, 46321, 31327, 83004, 62333, 76130, 71076, 4479, 3902, 72004, 51841, 80515, 81991, 44433, 88682, 57233, 61050, 41366, 41982, 3767, 47786, 44265, 15617, 82443, 49355, 79521, 31316, 13883, 75859, 43512, 87051, 58478, 97849, 60504, 77335, 79927, 50373, 7214, 54517, 87047, 6953, 86674, 55400, 90111, 13012, 11948, 57702, 4055, 2962, 93442, 10776, 97910, 38378, 7379, 53392, 61519, 92347, 13588, 30645, 8792, 13344, 8208, 74486, 98713, 38436, 89368, 69686, 11229, 52530, 54736, 30962, 56773, 59506, 61866, 94428, 24575, 87058, 90944, 91095, 15154, 36446, 8686, 5010, 77459, 77404, 50557, 86488, 13122, 536, 44928, 61466, 95127, 24192, 78391, 30282, 72166, 36046, 45395, 10200, 12275, 17171, 66459, 24543, 94819, 96561, 22637, 40030, 59489, 31403, 10131, 8241, 78186, 92811, 15189, 57851, 63451, 81199, 4584, 66235, 46659, 30475, 69218, 18685, 28082, 44455, 9355, 71838, 82437, 29512, 97628, 12092, 29048, 61948, 48401, 44599, 68714, 81130, 289, 85369, 76630, 31940, 22903]

def createArray(arrLen):
    arrResult = []
    for i in range(arrLen):
        arrResult.append(random.randint(1,arrLen))
    return arrResult

def createNoDupArray(arrLen):
    arrResult = []
    for i in range(arrLen):
        arrResult.append(i)
    arrResult.append(i)
    return arrResult

def firstDuplicate(a):
    print(len(a))
    set_a = frozenset(a)
    set_a1 = set()
    least_dup = len(a)-1
    print(len(set_a))
    dup = {}
    for z in set_a:
        if a.count(z) > 1:
          dup[z] = [i for i,x in enumerate(a) if x==z]
    print(dup)


def checkDups(a):
    for j in set(dups):
        first_occ_ind = a.index(j)
        a.remove(j)
        second_occ_ind = a.index(j)+1
        a.insert(first_occ_ind,j)
        if second_occ_ind < least_dup:
            least_dup = second_occ_ind

    if least_dup == len(a)-1:
        return -1
    else:
        return a[least_dup]

#[i for i,x in enumerate(a) if x==2]

def firstHDuplicate(a):
    set_a = frozenset(a)
    h_a = map(hash, a)
    check_arr = []
    res = -1
    #print(h_a)
    if len(a) != len(set_a):
        for entry in h_a:
            if entry in check_arr:
                res = entry
                break
            else:
                check_arr.append(entry)
    return res


def firstHHDuplicate(a):
    check_arr = {}
    res = -1
    for entry in a:
        if entry in check_arr:
            res = entry
            break
        else:
            check_arr[entry] = True
            #check_arr.append(entry)
    return res


#my_a = createArray(10000)
#firstDuplicate(createArray(500))
#print(firstHDuplicate(createArray(1000000)))
print(firstHHDuplicate(createNoDupArray(9999999)))
#print(firstHDuplicate(a))