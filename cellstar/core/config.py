# -*- coding: utf-8 -*-
"""
Config is a storage for default CellStar configuration.
Date: 2013-2016
Website: http://cellstar-algorithm.org/
"""


def default_config():
    return {
        'segmentation': {
            'foreground': {
                'FillHolesWithAreaSmallerThan': 2.26,
                'MaskDilation': 0.136,
                'MaskMinRadius': 0.34,
                'MaskThreshold': 0.03,
                'pickyDetection': False,
                'blur': 1,
                'MinCellClusterArea': 0.85
            },
            'avgCellDiameter': 35,
            'background': {
                'blurSteps': 50,
                'computeByBlurring': 0.5,
                'blur': 0.3
            },
            'ranking': {
                'avgInnerBrightnessWeight': 10,
                'avgBorderBrightnessWeight': 300,
                'stickingWeight': 60,
                'shift': 0.68,
                'maxInnerBrightnessWeight': 10,
                'logAreaBonus': 18,
                'maxRank': 100,
                'avgInnerDarknessWeight': 0
            },
            'minArea': 0.07,
            'cellBorder': {
                'medianFilter': 0.1
            },
            'maxFreeBorder': 0.4,
            'cellContent': {
                'MaskThreshold': 0.0,
                'medianFilter': 0.17,
                'blur': 0.6
            },
            'steps': 2,
            'maxArea': 2.83,
            'stars': {
                'cumBrightnessWeight': 304.45,
                'maxSize': 1.67,
                'gradientWeight': 15.482,
                'sizeWeight': [189.4082],
                'brightnessWeight': 0.0442,
                'step': 0.0335,
                'points': 28,
                'borderThickness': 0.1,
                'unstick': 0.3,
                'backgroundWeight': 0.0,
                'smoothness': 7.0,
                'gradientBlur': 0.0
            },
            'minAvgInnerDarkness': 0.1,
            'maxOverlap': 0.3,
            'seeding': {
                'from': {
                    'cellContentRandom': 0,
                    'cellBorderRemovingCurrSegmentsRandom': 0,
                    'cellContentRemovingCurrSegments': 1,
                    'snakesCentroids': 0,
                    'cellContent': 0,
                    'cellContentRemovingCurrSegmentsRandom': 0,
                    'cellBorderRemovingCurrSegments': 0,
                    'cellBorder': 1,
                    'snakesCentroidsRandom': 0,
                    'cellBorderRandom': 0
                },
                'ContentBlur': 2,
                'randomDiskRadius': 0.33,
                'minDistance': 0.27,
                'BorderBlur': 2
            }
        }
    }
