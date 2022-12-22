import sys

example = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

actual = """520,96 -> 520,92 -> 520,96 -> 522,96 -> 522,86 -> 522,96 -> 524,96 -> 524,92 -> 524,96 -> 526,96 -> 526,93 -> 526,96 -> 528,96 -> 528,95 -> 528,96 -> 530,96 -> 530,88 -> 530,96 -> 532,96 -> 532,88 -> 532,96 -> 534,96 -> 534,91 -> 534,96 -> 536,96 -> 536,92 -> 536,96 -> 538,96 -> 538,88 -> 538,96
490,15 -> 501,15 -> 501,14
503,68 -> 508,68
513,60 -> 513,61 -> 523,61 -> 523,60
503,37 -> 503,31 -> 503,37 -> 505,37 -> 505,29 -> 505,37 -> 507,37 -> 507,29 -> 507,37 -> 509,37 -> 509,29 -> 509,37 -> 511,37 -> 511,32 -> 511,37 -> 513,37 -> 513,29 -> 513,37 -> 515,37 -> 515,34 -> 515,37 -> 517,37 -> 517,36 -> 517,37 -> 519,37 -> 519,36 -> 519,37
524,136 -> 529,136
520,96 -> 520,92 -> 520,96 -> 522,96 -> 522,86 -> 522,96 -> 524,96 -> 524,92 -> 524,96 -> 526,96 -> 526,93 -> 526,96 -> 528,96 -> 528,95 -> 528,96 -> 530,96 -> 530,88 -> 530,96 -> 532,96 -> 532,88 -> 532,96 -> 534,96 -> 534,91 -> 534,96 -> 536,96 -> 536,92 -> 536,96 -> 538,96 -> 538,88 -> 538,96
509,64 -> 514,64
529,159 -> 529,153 -> 529,159 -> 531,159 -> 531,151 -> 531,159 -> 533,159 -> 533,156 -> 533,159 -> 535,159 -> 535,152 -> 535,159 -> 537,159 -> 537,154 -> 537,159 -> 539,159 -> 539,156 -> 539,159
518,46 -> 522,46
529,159 -> 529,153 -> 529,159 -> 531,159 -> 531,151 -> 531,159 -> 533,159 -> 533,156 -> 533,159 -> 535,159 -> 535,152 -> 535,159 -> 537,159 -> 537,154 -> 537,159 -> 539,159 -> 539,156 -> 539,159
520,96 -> 520,92 -> 520,96 -> 522,96 -> 522,86 -> 522,96 -> 524,96 -> 524,92 -> 524,96 -> 526,96 -> 526,93 -> 526,96 -> 528,96 -> 528,95 -> 528,96 -> 530,96 -> 530,88 -> 530,96 -> 532,96 -> 532,88 -> 532,96 -> 534,96 -> 534,91 -> 534,96 -> 536,96 -> 536,92 -> 536,96 -> 538,96 -> 538,88 -> 538,96
521,71 -> 521,73 -> 514,73 -> 514,79 -> 527,79 -> 527,73 -> 525,73 -> 525,71
503,37 -> 503,31 -> 503,37 -> 505,37 -> 505,29 -> 505,37 -> 507,37 -> 507,29 -> 507,37 -> 509,37 -> 509,29 -> 509,37 -> 511,37 -> 511,32 -> 511,37 -> 513,37 -> 513,29 -> 513,37 -> 515,37 -> 515,34 -> 515,37 -> 517,37 -> 517,36 -> 517,37 -> 519,37 -> 519,36 -> 519,37
532,109 -> 532,103 -> 532,109 -> 534,109 -> 534,106 -> 534,109 -> 536,109 -> 536,102 -> 536,109 -> 538,109 -> 538,107 -> 538,109 -> 540,109 -> 540,107 -> 540,109 -> 542,109 -> 542,100 -> 542,109 -> 544,109 -> 544,106 -> 544,109
532,109 -> 532,103 -> 532,109 -> 534,109 -> 534,106 -> 534,109 -> 536,109 -> 536,102 -> 536,109 -> 538,109 -> 538,107 -> 538,109 -> 540,109 -> 540,107 -> 540,109 -> 542,109 -> 542,100 -> 542,109 -> 544,109 -> 544,106 -> 544,109
518,82 -> 518,83 -> 529,83 -> 529,82
530,124 -> 535,124
520,96 -> 520,92 -> 520,96 -> 522,96 -> 522,86 -> 522,96 -> 524,96 -> 524,92 -> 524,96 -> 526,96 -> 526,93 -> 526,96 -> 528,96 -> 528,95 -> 528,96 -> 530,96 -> 530,88 -> 530,96 -> 532,96 -> 532,88 -> 532,96 -> 534,96 -> 534,91 -> 534,96 -> 536,96 -> 536,92 -> 536,96 -> 538,96 -> 538,88 -> 538,96
532,109 -> 532,103 -> 532,109 -> 534,109 -> 534,106 -> 534,109 -> 536,109 -> 536,102 -> 536,109 -> 538,109 -> 538,107 -> 538,109 -> 540,109 -> 540,107 -> 540,109 -> 542,109 -> 542,100 -> 542,109 -> 544,109 -> 544,106 -> 544,109
503,37 -> 503,31 -> 503,37 -> 505,37 -> 505,29 -> 505,37 -> 507,37 -> 507,29 -> 507,37 -> 509,37 -> 509,29 -> 509,37 -> 511,37 -> 511,32 -> 511,37 -> 513,37 -> 513,29 -> 513,37 -> 515,37 -> 515,34 -> 515,37 -> 517,37 -> 517,36 -> 517,37 -> 519,37 -> 519,36 -> 519,37
542,112 -> 547,112
536,118 -> 541,118
529,159 -> 529,153 -> 529,159 -> 531,159 -> 531,151 -> 531,159 -> 533,159 -> 533,156 -> 533,159 -> 535,159 -> 535,152 -> 535,159 -> 537,159 -> 537,154 -> 537,159 -> 539,159 -> 539,156 -> 539,159
528,139 -> 528,141 -> 521,141 -> 521,146 -> 534,146 -> 534,141 -> 531,141 -> 531,139
534,133 -> 539,133
543,118 -> 548,118
508,49 -> 508,52 -> 504,52 -> 504,55 -> 516,55 -> 516,52 -> 514,52 -> 514,49
532,109 -> 532,103 -> 532,109 -> 534,109 -> 534,106 -> 534,109 -> 536,109 -> 536,102 -> 536,109 -> 538,109 -> 538,107 -> 538,109 -> 540,109 -> 540,107 -> 540,109 -> 542,109 -> 542,100 -> 542,109 -> 544,109 -> 544,106 -> 544,109
508,49 -> 508,52 -> 504,52 -> 504,55 -> 516,55 -> 516,52 -> 514,52 -> 514,49
503,37 -> 503,31 -> 503,37 -> 505,37 -> 505,29 -> 505,37 -> 507,37 -> 507,29 -> 507,37 -> 509,37 -> 509,29 -> 509,37 -> 511,37 -> 511,32 -> 511,37 -> 513,37 -> 513,29 -> 513,37 -> 515,37 -> 515,34 -> 515,37 -> 517,37 -> 517,36 -> 517,37 -> 519,37 -> 519,36 -> 519,37
500,18 -> 500,20 -> 496,20 -> 496,24 -> 511,24 -> 511,20 -> 504,20 -> 504,18
530,130 -> 535,130
520,96 -> 520,92 -> 520,96 -> 522,96 -> 522,86 -> 522,96 -> 524,96 -> 524,92 -> 524,96 -> 526,96 -> 526,93 -> 526,96 -> 528,96 -> 528,95 -> 528,96 -> 530,96 -> 530,88 -> 530,96 -> 532,96 -> 532,88 -> 532,96 -> 534,96 -> 534,91 -> 534,96 -> 536,96 -> 536,92 -> 536,96 -> 538,96 -> 538,88 -> 538,96
508,49 -> 508,52 -> 504,52 -> 504,55 -> 516,55 -> 516,52 -> 514,52 -> 514,49
520,96 -> 520,92 -> 520,96 -> 522,96 -> 522,86 -> 522,96 -> 524,96 -> 524,92 -> 524,96 -> 526,96 -> 526,93 -> 526,96 -> 528,96 -> 528,95 -> 528,96 -> 530,96 -> 530,88 -> 530,96 -> 532,96 -> 532,88 -> 532,96 -> 534,96 -> 534,91 -> 534,96 -> 536,96 -> 536,92 -> 536,96 -> 538,96 -> 538,88 -> 538,96
532,109 -> 532,103 -> 532,109 -> 534,109 -> 534,106 -> 534,109 -> 536,109 -> 536,102 -> 536,109 -> 538,109 -> 538,107 -> 538,109 -> 540,109 -> 540,107 -> 540,109 -> 542,109 -> 542,100 -> 542,109 -> 544,109 -> 544,106 -> 544,109
503,37 -> 503,31 -> 503,37 -> 505,37 -> 505,29 -> 505,37 -> 507,37 -> 507,29 -> 507,37 -> 509,37 -> 509,29 -> 509,37 -> 511,37 -> 511,32 -> 511,37 -> 513,37 -> 513,29 -> 513,37 -> 515,37 -> 515,34 -> 515,37 -> 517,37 -> 517,36 -> 517,37 -> 519,37 -> 519,36 -> 519,37
546,115 -> 551,115
524,46 -> 528,46
532,109 -> 532,103 -> 532,109 -> 534,109 -> 534,106 -> 534,109 -> 536,109 -> 536,102 -> 536,109 -> 538,109 -> 538,107 -> 538,109 -> 540,109 -> 540,107 -> 540,109 -> 542,109 -> 542,100 -> 542,109 -> 544,109 -> 544,106 -> 544,109
520,96 -> 520,92 -> 520,96 -> 522,96 -> 522,86 -> 522,96 -> 524,96 -> 524,92 -> 524,96 -> 526,96 -> 526,93 -> 526,96 -> 528,96 -> 528,95 -> 528,96 -> 530,96 -> 530,88 -> 530,96 -> 532,96 -> 532,88 -> 532,96 -> 534,96 -> 534,91 -> 534,96 -> 536,96 -> 536,92 -> 536,96 -> 538,96 -> 538,88 -> 538,96
521,71 -> 521,73 -> 514,73 -> 514,79 -> 527,79 -> 527,73 -> 525,73 -> 525,71
520,96 -> 520,92 -> 520,96 -> 522,96 -> 522,86 -> 522,96 -> 524,96 -> 524,92 -> 524,96 -> 526,96 -> 526,93 -> 526,96 -> 528,96 -> 528,95 -> 528,96 -> 530,96 -> 530,88 -> 530,96 -> 532,96 -> 532,88 -> 532,96 -> 534,96 -> 534,91 -> 534,96 -> 536,96 -> 536,92 -> 536,96 -> 538,96 -> 538,88 -> 538,96
503,37 -> 503,31 -> 503,37 -> 505,37 -> 505,29 -> 505,37 -> 507,37 -> 507,29 -> 507,37 -> 509,37 -> 509,29 -> 509,37 -> 511,37 -> 511,32 -> 511,37 -> 513,37 -> 513,29 -> 513,37 -> 515,37 -> 515,34 -> 515,37 -> 517,37 -> 517,36 -> 517,37 -> 519,37 -> 519,36 -> 519,37
503,37 -> 503,31 -> 503,37 -> 505,37 -> 505,29 -> 505,37 -> 507,37 -> 507,29 -> 507,37 -> 509,37 -> 509,29 -> 509,37 -> 511,37 -> 511,32 -> 511,37 -> 513,37 -> 513,29 -> 513,37 -> 515,37 -> 515,34 -> 515,37 -> 517,37 -> 517,36 -> 517,37 -> 519,37 -> 519,36 -> 519,37
537,124 -> 542,124
532,109 -> 532,103 -> 532,109 -> 534,109 -> 534,106 -> 534,109 -> 536,109 -> 536,102 -> 536,109 -> 538,109 -> 538,107 -> 538,109 -> 540,109 -> 540,107 -> 540,109 -> 542,109 -> 542,100 -> 542,109 -> 544,109 -> 544,106 -> 544,109
529,159 -> 529,153 -> 529,159 -> 531,159 -> 531,151 -> 531,159 -> 533,159 -> 533,156 -> 533,159 -> 535,159 -> 535,152 -> 535,159 -> 537,159 -> 537,154 -> 537,159 -> 539,159 -> 539,156 -> 539,159
528,139 -> 528,141 -> 521,141 -> 521,146 -> 534,146 -> 534,141 -> 531,141 -> 531,139
500,18 -> 500,20 -> 496,20 -> 496,24 -> 511,24 -> 511,20 -> 504,20 -> 504,18
539,115 -> 544,115
503,37 -> 503,31 -> 503,37 -> 505,37 -> 505,29 -> 505,37 -> 507,37 -> 507,29 -> 507,37 -> 509,37 -> 509,29 -> 509,37 -> 511,37 -> 511,32 -> 511,37 -> 513,37 -> 513,29 -> 513,37 -> 515,37 -> 515,34 -> 515,37 -> 517,37 -> 517,36 -> 517,37 -> 519,37 -> 519,36 -> 519,37
503,37 -> 503,31 -> 503,37 -> 505,37 -> 505,29 -> 505,37 -> 507,37 -> 507,29 -> 507,37 -> 509,37 -> 509,29 -> 509,37 -> 511,37 -> 511,32 -> 511,37 -> 513,37 -> 513,29 -> 513,37 -> 515,37 -> 515,34 -> 515,37 -> 517,37 -> 517,36 -> 517,37 -> 519,37 -> 519,36 -> 519,37
521,71 -> 521,73 -> 514,73 -> 514,79 -> 527,79 -> 527,73 -> 525,73 -> 525,71
532,109 -> 532,103 -> 532,109 -> 534,109 -> 534,106 -> 534,109 -> 536,109 -> 536,102 -> 536,109 -> 538,109 -> 538,107 -> 538,109 -> 540,109 -> 540,107 -> 540,109 -> 542,109 -> 542,100 -> 542,109 -> 544,109 -> 544,106 -> 544,109
520,96 -> 520,92 -> 520,96 -> 522,96 -> 522,86 -> 522,96 -> 524,96 -> 524,92 -> 524,96 -> 526,96 -> 526,93 -> 526,96 -> 528,96 -> 528,95 -> 528,96 -> 530,96 -> 530,88 -> 530,96 -> 532,96 -> 532,88 -> 532,96 -> 534,96 -> 534,91 -> 534,96 -> 536,96 -> 536,92 -> 536,96 -> 538,96 -> 538,88 -> 538,96
520,96 -> 520,92 -> 520,96 -> 522,96 -> 522,86 -> 522,96 -> 524,96 -> 524,92 -> 524,96 -> 526,96 -> 526,93 -> 526,96 -> 528,96 -> 528,95 -> 528,96 -> 530,96 -> 530,88 -> 530,96 -> 532,96 -> 532,88 -> 532,96 -> 534,96 -> 534,91 -> 534,96 -> 536,96 -> 536,92 -> 536,96 -> 538,96 -> 538,88 -> 538,96
533,127 -> 538,127
518,82 -> 518,83 -> 529,83 -> 529,82
503,37 -> 503,31 -> 503,37 -> 505,37 -> 505,29 -> 505,37 -> 507,37 -> 507,29 -> 507,37 -> 509,37 -> 509,29 -> 509,37 -> 511,37 -> 511,32 -> 511,37 -> 513,37 -> 513,29 -> 513,37 -> 515,37 -> 515,34 -> 515,37 -> 517,37 -> 517,36 -> 517,37 -> 519,37 -> 519,36 -> 519,37
506,66 -> 511,66
503,37 -> 503,31 -> 503,37 -> 505,37 -> 505,29 -> 505,37 -> 507,37 -> 507,29 -> 507,37 -> 509,37 -> 509,29 -> 509,37 -> 511,37 -> 511,32 -> 511,37 -> 513,37 -> 513,29 -> 513,37 -> 515,37 -> 515,34 -> 515,37 -> 517,37 -> 517,36 -> 517,37 -> 519,37 -> 519,36 -> 519,37
535,161 -> 535,162 -> 544,162 -> 544,161
529,159 -> 529,153 -> 529,159 -> 531,159 -> 531,151 -> 531,159 -> 533,159 -> 533,156 -> 533,159 -> 535,159 -> 535,152 -> 535,159 -> 537,159 -> 537,154 -> 537,159 -> 539,159 -> 539,156 -> 539,159
500,18 -> 500,20 -> 496,20 -> 496,24 -> 511,24 -> 511,20 -> 504,20 -> 504,18
520,96 -> 520,92 -> 520,96 -> 522,96 -> 522,86 -> 522,96 -> 524,96 -> 524,92 -> 524,96 -> 526,96 -> 526,93 -> 526,96 -> 528,96 -> 528,95 -> 528,96 -> 530,96 -> 530,88 -> 530,96 -> 532,96 -> 532,88 -> 532,96 -> 534,96 -> 534,91 -> 534,96 -> 536,96 -> 536,92 -> 536,96 -> 538,96 -> 538,88 -> 538,96
520,96 -> 520,92 -> 520,96 -> 522,96 -> 522,86 -> 522,96 -> 524,96 -> 524,92 -> 524,96 -> 526,96 -> 526,93 -> 526,96 -> 528,96 -> 528,95 -> 528,96 -> 530,96 -> 530,88 -> 530,96 -> 532,96 -> 532,88 -> 532,96 -> 534,96 -> 534,91 -> 534,96 -> 536,96 -> 536,92 -> 536,96 -> 538,96 -> 538,88 -> 538,96
503,37 -> 503,31 -> 503,37 -> 505,37 -> 505,29 -> 505,37 -> 507,37 -> 507,29 -> 507,37 -> 509,37 -> 509,29 -> 509,37 -> 511,37 -> 511,32 -> 511,37 -> 513,37 -> 513,29 -> 513,37 -> 515,37 -> 515,34 -> 515,37 -> 517,37 -> 517,36 -> 517,37 -> 519,37 -> 519,36 -> 519,37
490,15 -> 501,15 -> 501,14
535,161 -> 535,162 -> 544,162 -> 544,161
508,49 -> 508,52 -> 504,52 -> 504,55 -> 516,55 -> 516,52 -> 514,52 -> 514,49
518,82 -> 518,83 -> 529,83 -> 529,82
513,66 -> 518,66
532,109 -> 532,103 -> 532,109 -> 534,109 -> 534,106 -> 534,109 -> 536,109 -> 536,102 -> 536,109 -> 538,109 -> 538,107 -> 538,109 -> 540,109 -> 540,107 -> 540,109 -> 542,109 -> 542,100 -> 542,109 -> 544,109 -> 544,106 -> 544,109
532,109 -> 532,103 -> 532,109 -> 534,109 -> 534,106 -> 534,109 -> 536,109 -> 536,102 -> 536,109 -> 538,109 -> 538,107 -> 538,109 -> 540,109 -> 540,107 -> 540,109 -> 542,109 -> 542,100 -> 542,109 -> 544,109 -> 544,106 -> 544,109
558,124 -> 563,124
520,96 -> 520,92 -> 520,96 -> 522,96 -> 522,86 -> 522,96 -> 524,96 -> 524,92 -> 524,96 -> 526,96 -> 526,93 -> 526,96 -> 528,96 -> 528,95 -> 528,96 -> 530,96 -> 530,88 -> 530,96 -> 532,96 -> 532,88 -> 532,96 -> 534,96 -> 534,91 -> 534,96 -> 536,96 -> 536,92 -> 536,96 -> 538,96 -> 538,88 -> 538,96
532,109 -> 532,103 -> 532,109 -> 534,109 -> 534,106 -> 534,109 -> 536,109 -> 536,102 -> 536,109 -> 538,109 -> 538,107 -> 538,109 -> 540,109 -> 540,107 -> 540,109 -> 542,109 -> 542,100 -> 542,109 -> 544,109 -> 544,106 -> 544,109
532,109 -> 532,103 -> 532,109 -> 534,109 -> 534,106 -> 534,109 -> 536,109 -> 536,102 -> 536,109 -> 538,109 -> 538,107 -> 538,109 -> 540,109 -> 540,107 -> 540,109 -> 542,109 -> 542,100 -> 542,109 -> 544,109 -> 544,106 -> 544,109
503,37 -> 503,31 -> 503,37 -> 505,37 -> 505,29 -> 505,37 -> 507,37 -> 507,29 -> 507,37 -> 509,37 -> 509,29 -> 509,37 -> 511,37 -> 511,32 -> 511,37 -> 513,37 -> 513,29 -> 513,37 -> 515,37 -> 515,34 -> 515,37 -> 517,37 -> 517,36 -> 517,37 -> 519,37 -> 519,36 -> 519,37
529,159 -> 529,153 -> 529,159 -> 531,159 -> 531,151 -> 531,159 -> 533,159 -> 533,156 -> 533,159 -> 535,159 -> 535,152 -> 535,159 -> 537,159 -> 537,154 -> 537,159 -> 539,159 -> 539,156 -> 539,159
528,139 -> 528,141 -> 521,141 -> 521,146 -> 534,146 -> 534,141 -> 531,141 -> 531,139
520,96 -> 520,92 -> 520,96 -> 522,96 -> 522,86 -> 522,96 -> 524,96 -> 524,92 -> 524,96 -> 526,96 -> 526,93 -> 526,96 -> 528,96 -> 528,95 -> 528,96 -> 530,96 -> 530,88 -> 530,96 -> 532,96 -> 532,88 -> 532,96 -> 534,96 -> 534,91 -> 534,96 -> 536,96 -> 536,92 -> 536,96 -> 538,96 -> 538,88 -> 538,96
529,159 -> 529,153 -> 529,159 -> 531,159 -> 531,151 -> 531,159 -> 533,159 -> 533,156 -> 533,159 -> 535,159 -> 535,152 -> 535,159 -> 537,159 -> 537,154 -> 537,159 -> 539,159 -> 539,156 -> 539,159
520,96 -> 520,92 -> 520,96 -> 522,96 -> 522,86 -> 522,96 -> 524,96 -> 524,92 -> 524,96 -> 526,96 -> 526,93 -> 526,96 -> 528,96 -> 528,95 -> 528,96 -> 530,96 -> 530,88 -> 530,96 -> 532,96 -> 532,88 -> 532,96 -> 534,96 -> 534,91 -> 534,96 -> 536,96 -> 536,92 -> 536,96 -> 538,96 -> 538,88 -> 538,96
554,121 -> 559,121
520,96 -> 520,92 -> 520,96 -> 522,96 -> 522,86 -> 522,96 -> 524,96 -> 524,92 -> 524,96 -> 526,96 -> 526,93 -> 526,96 -> 528,96 -> 528,95 -> 528,96 -> 530,96 -> 530,88 -> 530,96 -> 532,96 -> 532,88 -> 532,96 -> 534,96 -> 534,91 -> 534,96 -> 536,96 -> 536,92 -> 536,96 -> 538,96 -> 538,88 -> 538,96
508,49 -> 508,52 -> 504,52 -> 504,55 -> 516,55 -> 516,52 -> 514,52 -> 514,49
540,121 -> 545,121
520,96 -> 520,92 -> 520,96 -> 522,96 -> 522,86 -> 522,96 -> 524,96 -> 524,92 -> 524,96 -> 526,96 -> 526,93 -> 526,96 -> 528,96 -> 528,95 -> 528,96 -> 530,96 -> 530,88 -> 530,96 -> 532,96 -> 532,88 -> 532,96 -> 534,96 -> 534,91 -> 534,96 -> 536,96 -> 536,92 -> 536,96 -> 538,96 -> 538,88 -> 538,96
503,37 -> 503,31 -> 503,37 -> 505,37 -> 505,29 -> 505,37 -> 507,37 -> 507,29 -> 507,37 -> 509,37 -> 509,29 -> 509,37 -> 511,37 -> 511,32 -> 511,37 -> 513,37 -> 513,29 -> 513,37 -> 515,37 -> 515,34 -> 515,37 -> 517,37 -> 517,36 -> 517,37 -> 519,37 -> 519,36 -> 519,37
529,159 -> 529,153 -> 529,159 -> 531,159 -> 531,151 -> 531,159 -> 533,159 -> 533,156 -> 533,159 -> 535,159 -> 535,152 -> 535,159 -> 537,159 -> 537,154 -> 537,159 -> 539,159 -> 539,156 -> 539,159
529,159 -> 529,153 -> 529,159 -> 531,159 -> 531,151 -> 531,159 -> 533,159 -> 533,156 -> 533,159 -> 535,159 -> 535,152 -> 535,159 -> 537,159 -> 537,154 -> 537,159 -> 539,159 -> 539,156 -> 539,159
547,121 -> 552,121
503,37 -> 503,31 -> 503,37 -> 505,37 -> 505,29 -> 505,37 -> 507,37 -> 507,29 -> 507,37 -> 509,37 -> 509,29 -> 509,37 -> 511,37 -> 511,32 -> 511,37 -> 513,37 -> 513,29 -> 513,37 -> 515,37 -> 515,34 -> 515,37 -> 517,37 -> 517,36 -> 517,37 -> 519,37 -> 519,36 -> 519,37
503,37 -> 503,31 -> 503,37 -> 505,37 -> 505,29 -> 505,37 -> 507,37 -> 507,29 -> 507,37 -> 509,37 -> 509,29 -> 509,37 -> 511,37 -> 511,32 -> 511,37 -> 513,37 -> 513,29 -> 513,37 -> 515,37 -> 515,34 -> 515,37 -> 517,37 -> 517,36 -> 517,37 -> 519,37 -> 519,36 -> 519,37
520,96 -> 520,92 -> 520,96 -> 522,96 -> 522,86 -> 522,96 -> 524,96 -> 524,92 -> 524,96 -> 526,96 -> 526,93 -> 526,96 -> 528,96 -> 528,95 -> 528,96 -> 530,96 -> 530,88 -> 530,96 -> 532,96 -> 532,88 -> 532,96 -> 534,96 -> 534,91 -> 534,96 -> 536,96 -> 536,92 -> 536,96 -> 538,96 -> 538,88 -> 538,96
503,37 -> 503,31 -> 503,37 -> 505,37 -> 505,29 -> 505,37 -> 507,37 -> 507,29 -> 507,37 -> 509,37 -> 509,29 -> 509,37 -> 511,37 -> 511,32 -> 511,37 -> 513,37 -> 513,29 -> 513,37 -> 515,37 -> 515,34 -> 515,37 -> 517,37 -> 517,36 -> 517,37 -> 519,37 -> 519,36 -> 519,37
500,18 -> 500,20 -> 496,20 -> 496,24 -> 511,24 -> 511,20 -> 504,20 -> 504,18
532,109 -> 532,103 -> 532,109 -> 534,109 -> 534,106 -> 534,109 -> 536,109 -> 536,102 -> 536,109 -> 538,109 -> 538,107 -> 538,109 -> 540,109 -> 540,107 -> 540,109 -> 542,109 -> 542,100 -> 542,109 -> 544,109 -> 544,106 -> 544,109
529,159 -> 529,153 -> 529,159 -> 531,159 -> 531,151 -> 531,159 -> 533,159 -> 533,156 -> 533,159 -> 535,159 -> 535,152 -> 535,159 -> 537,159 -> 537,154 -> 537,159 -> 539,159 -> 539,156 -> 539,159
512,46 -> 516,46
544,124 -> 549,124
503,37 -> 503,31 -> 503,37 -> 505,37 -> 505,29 -> 505,37 -> 507,37 -> 507,29 -> 507,37 -> 509,37 -> 509,29 -> 509,37 -> 511,37 -> 511,32 -> 511,37 -> 513,37 -> 513,29 -> 513,37 -> 515,37 -> 515,34 -> 515,37 -> 517,37 -> 517,36 -> 517,37 -> 519,37 -> 519,36 -> 519,37
521,71 -> 521,73 -> 514,73 -> 514,79 -> 527,79 -> 527,73 -> 525,73 -> 525,71
532,109 -> 532,103 -> 532,109 -> 534,109 -> 534,106 -> 534,109 -> 536,109 -> 536,102 -> 536,109 -> 538,109 -> 538,107 -> 538,109 -> 540,109 -> 540,107 -> 540,109 -> 542,109 -> 542,100 -> 542,109 -> 544,109 -> 544,106 -> 544,109
528,139 -> 528,141 -> 521,141 -> 521,146 -> 534,146 -> 534,141 -> 531,141 -> 531,139
520,96 -> 520,92 -> 520,96 -> 522,96 -> 522,86 -> 522,96 -> 524,96 -> 524,92 -> 524,96 -> 526,96 -> 526,93 -> 526,96 -> 528,96 -> 528,95 -> 528,96 -> 530,96 -> 530,88 -> 530,96 -> 532,96 -> 532,88 -> 532,96 -> 534,96 -> 534,91 -> 534,96 -> 536,96 -> 536,92 -> 536,96 -> 538,96 -> 538,88 -> 538,96
528,139 -> 528,141 -> 521,141 -> 521,146 -> 534,146 -> 534,141 -> 531,141 -> 531,139
533,121 -> 538,121
503,37 -> 503,31 -> 503,37 -> 505,37 -> 505,29 -> 505,37 -> 507,37 -> 507,29 -> 507,37 -> 509,37 -> 509,29 -> 509,37 -> 511,37 -> 511,32 -> 511,37 -> 513,37 -> 513,29 -> 513,37 -> 515,37 -> 515,34 -> 515,37 -> 517,37 -> 517,36 -> 517,37 -> 519,37 -> 519,36 -> 519,37
521,43 -> 525,43
500,18 -> 500,20 -> 496,20 -> 496,24 -> 511,24 -> 511,20 -> 504,20 -> 504,18
527,133 -> 532,133
503,37 -> 503,31 -> 503,37 -> 505,37 -> 505,29 -> 505,37 -> 507,37 -> 507,29 -> 507,37 -> 509,37 -> 509,29 -> 509,37 -> 511,37 -> 511,32 -> 511,37 -> 513,37 -> 513,29 -> 513,37 -> 515,37 -> 515,34 -> 515,37 -> 517,37 -> 517,36 -> 517,37 -> 519,37 -> 519,36 -> 519,37
503,37 -> 503,31 -> 503,37 -> 505,37 -> 505,29 -> 505,37 -> 507,37 -> 507,29 -> 507,37 -> 509,37 -> 509,29 -> 509,37 -> 511,37 -> 511,32 -> 511,37 -> 513,37 -> 513,29 -> 513,37 -> 515,37 -> 515,34 -> 515,37 -> 517,37 -> 517,36 -> 517,37 -> 519,37 -> 519,36 -> 519,37
529,159 -> 529,153 -> 529,159 -> 531,159 -> 531,151 -> 531,159 -> 533,159 -> 533,156 -> 533,159 -> 535,159 -> 535,152 -> 535,159 -> 537,159 -> 537,154 -> 537,159 -> 539,159 -> 539,156 -> 539,159
520,96 -> 520,92 -> 520,96 -> 522,96 -> 522,86 -> 522,96 -> 524,96 -> 524,92 -> 524,96 -> 526,96 -> 526,93 -> 526,96 -> 528,96 -> 528,95 -> 528,96 -> 530,96 -> 530,88 -> 530,96 -> 532,96 -> 532,88 -> 532,96 -> 534,96 -> 534,91 -> 534,96 -> 536,96 -> 536,92 -> 536,96 -> 538,96 -> 538,88 -> 538,96
531,136 -> 536,136
503,37 -> 503,31 -> 503,37 -> 505,37 -> 505,29 -> 505,37 -> 507,37 -> 507,29 -> 507,37 -> 509,37 -> 509,29 -> 509,37 -> 511,37 -> 511,32 -> 511,37 -> 513,37 -> 513,29 -> 513,37 -> 515,37 -> 515,34 -> 515,37 -> 517,37 -> 517,36 -> 517,37 -> 519,37 -> 519,36 -> 519,37
515,43 -> 519,43
532,109 -> 532,103 -> 532,109 -> 534,109 -> 534,106 -> 534,109 -> 536,109 -> 536,102 -> 536,109 -> 538,109 -> 538,107 -> 538,109 -> 540,109 -> 540,107 -> 540,109 -> 542,109 -> 542,100 -> 542,109 -> 544,109 -> 544,106 -> 544,109
532,109 -> 532,103 -> 532,109 -> 534,109 -> 534,106 -> 534,109 -> 536,109 -> 536,102 -> 536,109 -> 538,109 -> 538,107 -> 538,109 -> 540,109 -> 540,107 -> 540,109 -> 542,109 -> 542,100 -> 542,109 -> 544,109 -> 544,106 -> 544,109
503,37 -> 503,31 -> 503,37 -> 505,37 -> 505,29 -> 505,37 -> 507,37 -> 507,29 -> 507,37 -> 509,37 -> 509,29 -> 509,37 -> 511,37 -> 511,32 -> 511,37 -> 513,37 -> 513,29 -> 513,37 -> 515,37 -> 515,34 -> 515,37 -> 517,37 -> 517,36 -> 517,37 -> 519,37 -> 519,36 -> 519,37
521,71 -> 521,73 -> 514,73 -> 514,79 -> 527,79 -> 527,73 -> 525,73 -> 525,71
521,71 -> 521,73 -> 514,73 -> 514,79 -> 527,79 -> 527,73 -> 525,73 -> 525,71
513,60 -> 513,61 -> 523,61 -> 523,60
503,37 -> 503,31 -> 503,37 -> 505,37 -> 505,29 -> 505,37 -> 507,37 -> 507,29 -> 507,37 -> 509,37 -> 509,29 -> 509,37 -> 511,37 -> 511,32 -> 511,37 -> 513,37 -> 513,29 -> 513,37 -> 515,37 -> 515,34 -> 515,37 -> 517,37 -> 517,36 -> 517,37 -> 519,37 -> 519,36 -> 519,37
537,130 -> 542,130
520,96 -> 520,92 -> 520,96 -> 522,96 -> 522,86 -> 522,96 -> 524,96 -> 524,92 -> 524,96 -> 526,96 -> 526,93 -> 526,96 -> 528,96 -> 528,95 -> 528,96 -> 530,96 -> 530,88 -> 530,96 -> 532,96 -> 532,88 -> 532,96 -> 534,96 -> 534,91 -> 534,96 -> 536,96 -> 536,92 -> 536,96 -> 538,96 -> 538,88 -> 538,96
508,49 -> 508,52 -> 504,52 -> 504,55 -> 516,55 -> 516,52 -> 514,52 -> 514,49
545,136 -> 550,136
538,136 -> 543,136
520,96 -> 520,92 -> 520,96 -> 522,96 -> 522,86 -> 522,96 -> 524,96 -> 524,92 -> 524,96 -> 526,96 -> 526,93 -> 526,96 -> 528,96 -> 528,95 -> 528,96 -> 530,96 -> 530,88 -> 530,96 -> 532,96 -> 532,88 -> 532,96 -> 534,96 -> 534,91 -> 534,96 -> 536,96 -> 536,92 -> 536,96 -> 538,96 -> 538,88 -> 538,96
532,109 -> 532,103 -> 532,109 -> 534,109 -> 534,106 -> 534,109 -> 536,109 -> 536,102 -> 536,109 -> 538,109 -> 538,107 -> 538,109 -> 540,109 -> 540,107 -> 540,109 -> 542,109 -> 542,100 -> 542,109 -> 544,109 -> 544,106 -> 544,109
528,139 -> 528,141 -> 521,141 -> 521,146 -> 534,146 -> 534,141 -> 531,141 -> 531,139
503,37 -> 503,31 -> 503,37 -> 505,37 -> 505,29 -> 505,37 -> 507,37 -> 507,29 -> 507,37 -> 509,37 -> 509,29 -> 509,37 -> 511,37 -> 511,32 -> 511,37 -> 513,37 -> 513,29 -> 513,37 -> 515,37 -> 515,34 -> 515,37 -> 517,37 -> 517,36 -> 517,37 -> 519,37 -> 519,36 -> 519,37
532,109 -> 532,103 -> 532,109 -> 534,109 -> 534,106 -> 534,109 -> 536,109 -> 536,102 -> 536,109 -> 538,109 -> 538,107 -> 538,109 -> 540,109 -> 540,107 -> 540,109 -> 542,109 -> 542,100 -> 542,109 -> 544,109 -> 544,106 -> 544,109
508,49 -> 508,52 -> 504,52 -> 504,55 -> 516,55 -> 516,52 -> 514,52 -> 514,49
532,109 -> 532,103 -> 532,109 -> 534,109 -> 534,106 -> 534,109 -> 536,109 -> 536,102 -> 536,109 -> 538,109 -> 538,107 -> 538,109 -> 540,109 -> 540,107 -> 540,109 -> 542,109 -> 542,100 -> 542,109 -> 544,109 -> 544,106 -> 544,109
503,37 -> 503,31 -> 503,37 -> 505,37 -> 505,29 -> 505,37 -> 507,37 -> 507,29 -> 507,37 -> 509,37 -> 509,29 -> 509,37 -> 511,37 -> 511,32 -> 511,37 -> 513,37 -> 513,29 -> 513,37 -> 515,37 -> 515,34 -> 515,37 -> 517,37 -> 517,36 -> 517,37 -> 519,37 -> 519,36 -> 519,37
529,159 -> 529,153 -> 529,159 -> 531,159 -> 531,151 -> 531,159 -> 533,159 -> 533,156 -> 533,159 -> 535,159 -> 535,152 -> 535,159 -> 537,159 -> 537,154 -> 537,159 -> 539,159 -> 539,156 -> 539,159
510,68 -> 515,68
520,96 -> 520,92 -> 520,96 -> 522,96 -> 522,86 -> 522,96 -> 524,96 -> 524,92 -> 524,96 -> 526,96 -> 526,93 -> 526,96 -> 528,96 -> 528,95 -> 528,96 -> 530,96 -> 530,88 -> 530,96 -> 532,96 -> 532,88 -> 532,96 -> 534,96 -> 534,91 -> 534,96 -> 536,96 -> 536,92 -> 536,96 -> 538,96 -> 538,88 -> 538,96
550,118 -> 555,118
520,96 -> 520,92 -> 520,96 -> 522,96 -> 522,86 -> 522,96 -> 524,96 -> 524,92 -> 524,96 -> 526,96 -> 526,93 -> 526,96 -> 528,96 -> 528,95 -> 528,96 -> 530,96 -> 530,88 -> 530,96 -> 532,96 -> 532,88 -> 532,96 -> 534,96 -> 534,91 -> 534,96 -> 536,96 -> 536,92 -> 536,96 -> 538,96 -> 538,88 -> 538,96
528,139 -> 528,141 -> 521,141 -> 521,146 -> 534,146 -> 534,141 -> 531,141 -> 531,139
529,159 -> 529,153 -> 529,159 -> 531,159 -> 531,151 -> 531,159 -> 533,159 -> 533,156 -> 533,159 -> 535,159 -> 535,152 -> 535,159 -> 537,159 -> 537,154 -> 537,159 -> 539,159 -> 539,156 -> 539,159
532,109 -> 532,103 -> 532,109 -> 534,109 -> 534,106 -> 534,109 -> 536,109 -> 536,102 -> 536,109 -> 538,109 -> 538,107 -> 538,109 -> 540,109 -> 540,107 -> 540,109 -> 542,109 -> 542,100 -> 542,109 -> 544,109 -> 544,106 -> 544,109
529,159 -> 529,153 -> 529,159 -> 531,159 -> 531,151 -> 531,159 -> 533,159 -> 533,156 -> 533,159 -> 535,159 -> 535,152 -> 535,159 -> 537,159 -> 537,154 -> 537,159 -> 539,159 -> 539,156 -> 539,159
521,71 -> 521,73 -> 514,73 -> 514,79 -> 527,79 -> 527,73 -> 525,73 -> 525,71
541,133 -> 546,133
529,159 -> 529,153 -> 529,159 -> 531,159 -> 531,151 -> 531,159 -> 533,159 -> 533,156 -> 533,159 -> 535,159 -> 535,152 -> 535,159 -> 537,159 -> 537,154 -> 537,159 -> 539,159 -> 539,156 -> 539,159
520,96 -> 520,92 -> 520,96 -> 522,96 -> 522,86 -> 522,96 -> 524,96 -> 524,92 -> 524,96 -> 526,96 -> 526,93 -> 526,96 -> 528,96 -> 528,95 -> 528,96 -> 530,96 -> 530,88 -> 530,96 -> 532,96 -> 532,88 -> 532,96 -> 534,96 -> 534,91 -> 534,96 -> 536,96 -> 536,92 -> 536,96 -> 538,96 -> 538,88 -> 538,96
513,60 -> 513,61 -> 523,61 -> 523,60
518,40 -> 522,40
517,68 -> 522,68
500,18 -> 500,20 -> 496,20 -> 496,24 -> 511,24 -> 511,20 -> 504,20 -> 504,18
520,96 -> 520,92 -> 520,96 -> 522,96 -> 522,86 -> 522,96 -> 524,96 -> 524,92 -> 524,96 -> 526,96 -> 526,93 -> 526,96 -> 528,96 -> 528,95 -> 528,96 -> 530,96 -> 530,88 -> 530,96 -> 532,96 -> 532,88 -> 532,96 -> 534,96 -> 534,91 -> 534,96 -> 536,96 -> 536,92 -> 536,96 -> 538,96 -> 538,88 -> 538,96
520,96 -> 520,92 -> 520,96 -> 522,96 -> 522,86 -> 522,96 -> 524,96 -> 524,92 -> 524,96 -> 526,96 -> 526,93 -> 526,96 -> 528,96 -> 528,95 -> 528,96 -> 530,96 -> 530,88 -> 530,96 -> 532,96 -> 532,88 -> 532,96 -> 534,96 -> 534,91 -> 534,96 -> 536,96 -> 536,92 -> 536,96 -> 538,96 -> 538,88 -> 538,96
529,159 -> 529,153 -> 529,159 -> 531,159 -> 531,151 -> 531,159 -> 533,159 -> 533,156 -> 533,159 -> 535,159 -> 535,152 -> 535,159 -> 537,159 -> 537,154 -> 537,159 -> 539,159 -> 539,156 -> 539,159
520,96 -> 520,92 -> 520,96 -> 522,96 -> 522,86 -> 522,96 -> 524,96 -> 524,92 -> 524,96 -> 526,96 -> 526,93 -> 526,96 -> 528,96 -> 528,95 -> 528,96 -> 530,96 -> 530,88 -> 530,96 -> 532,96 -> 532,88 -> 532,96 -> 534,96 -> 534,91 -> 534,96 -> 536,96 -> 536,92 -> 536,96 -> 538,96 -> 538,88 -> 538,96
520,96 -> 520,92 -> 520,96 -> 522,96 -> 522,86 -> 522,96 -> 524,96 -> 524,92 -> 524,96 -> 526,96 -> 526,93 -> 526,96 -> 528,96 -> 528,95 -> 528,96 -> 530,96 -> 530,88 -> 530,96 -> 532,96 -> 532,88 -> 532,96 -> 534,96 -> 534,91 -> 534,96 -> 536,96 -> 536,92 -> 536,96 -> 538,96 -> 538,88 -> 538,96
529,159 -> 529,153 -> 529,159 -> 531,159 -> 531,151 -> 531,159 -> 533,159 -> 533,156 -> 533,159 -> 535,159 -> 535,152 -> 535,159 -> 537,159 -> 537,154 -> 537,159 -> 539,159 -> 539,156 -> 539,159
535,161 -> 535,162 -> 544,162 -> 544,161
551,124 -> 556,124
500,18 -> 500,20 -> 496,20 -> 496,24 -> 511,24 -> 511,20 -> 504,20 -> 504,18"""

def parse(input):
    data = [line for line in input.split('\n')]
    result = []
    for line in data:
        result.append([[int(x.split(',')[0]), int(x.split(',')[1])] for x in line.split(' -> ')])

    min_x = sys.maxsize
    max_x = 0
    min_y = sys.maxsize
    max_y = 0
    for line in result:
        for point in line:
            if point[0] < min_x:
                min_x = point[0]
            # if point[1] < min_y:
            #     min_y = point[1]
            if point[0] > max_x:
                max_x = point[0]
            if point[1] > max_y:
                max_y = point[1]

    return result, {'min': {'x': 0, 'y': 0}, 'max': {'x': 1000, 'y': max_y + 3}}

def build_map(instructions, sizes):
    world = []
    for x in range(sizes['min']['x'], sizes['max']['x']):
        row = []
        for y in range(sizes['min']['y'], sizes['max']['y']):
            row.append(" ")
        world.append(row)

    for line in instructions:
        start = line[0]
        start = [start[0] - sizes['min']['x'], start[1]]

        for point in line[1:]:
            point = [point[0] - sizes['min']['x'], point[1]]

            xs = [start[0], point[0]]
            xs.sort()
            ys = [start[1], point[1]]
            ys.sort()

            for x in range(xs[0], xs[1] + 1):
                for y in range(ys[0], ys[1] + 1):
                    world[x][y] = '#'
            
            start = point

    for x in range(0, sizes['max']['x']):
        world[x][sizes['max']['y'] - 1] = '#'

    return world

def visualise(map, sizes):
    for y in range(0, sizes['max']['y']):
        for x in range(0, len(map)):
            print(map[x][y], end=' ')
        print()

def main(input):
    instructions, sizes = parse(input)

    map = build_map(instructions, sizes)

    # visualise(map, sizes)

    sand_source = 500 - sizes['min']['x']

    current_sand = {'x': sand_source, 'y': 0}

    while True:
        changed = False

        move_right = map[current_sand['x'] + 1][current_sand['y'] + 1] == ' '
        move_left = map[current_sand['x'] - 1][current_sand['y'] + 1] == ' '
        move_down = map[current_sand['x']][current_sand['y'] + 1] == ' '

        if move_down:
            map[current_sand['x']][current_sand['y']] = ' '
            current_sand['y'] = current_sand['y'] + 1
            map[current_sand['x']][current_sand['y']] = '.'
            changed = True

        elif move_left:
            map[current_sand['x']][current_sand['y']] = ' '
            current_sand['y'] = current_sand['y'] + 1
            current_sand['x'] = current_sand['x'] - 1
            map[current_sand['x']][current_sand['y']] = '.'
            changed = True

        elif move_right:
            map[current_sand['x']][current_sand['y']] = ' '
            current_sand['y'] = current_sand['y'] + 1
            current_sand['x'] = current_sand['x'] + 1
            map[current_sand['x']][current_sand['y']] = '.'
            changed = True


        if not changed:
            if map[sand_source][0] == '.':
                print("asdf", map[sand_source][0])
                break

            current_sand = {'x': sand_source, 'y': 0}
            map[current_sand['x']][current_sand['y']] = '.'

        if current_sand['y'] == len(map[0]) - 1:
            map[current_sand['x']][current_sand['y']] = ' '
            break

        # visualise(map, sizes)

    visualise(map, sizes)

    total = []
    sand = [[total.append(y) for y in x if y == '.'] for x in map]

    print(len(total))
    
if __name__ == '__main__':
    main(example)
    main(actual)