input.onButtonPressed(Button.A, function () {
    if (Mode == 0) {
        Score += -1
    }
})
input.onButtonPressed(Button.AB, function () {
    if (Mode == 0) {
        Mode = 1
    } else {
        Mode = 0
    }
})
input.onButtonPressed(Button.B, function () {
    if (Mode == 0) {
        Score += 1
    }
})
input.onGesture(Gesture.Shake, function () {
    if (Mode == 1) {
        RandomNum = randint(1, 6)
    }
})
let RandomNum = 0
let Mode = 0
Mode = 0
let Score = 0
basic.forever(function () {
    if (Mode == 0) {
        basic.showNumber(Score)
    } else {
        if (RandomNum == 1) {
            basic.showLeds(`
                . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
                `)
        } else if (RandomNum == 2) {
            basic.showLeds(`
                . . . . #
                . . . . .
                . . . . .
                . . . . .
                # . . . .
                `)
        } else if (RandomNum == 3) {
            basic.showLeds(`
                . . . . #
                . . . . .
                . . # . .
                . . . . .
                # . . . .
                `)
        } else if (RandomNum == 4) {
            basic.showLeds(`
                # . . . #
                . . . . .
                . . . . .
                . . . . .
                # . . . #
                `)
        } else if (RandomNum == 5) {
            basic.showLeds(`
                # . . . #
                . . . . .
                . . # . .
                . . . . .
                # . . . #
                `)
        } else {
            basic.showLeds(`
                # . # . #
                . . . . .
                . . . . .
                . . . . .
                # . # . #
                `)
        }
    }
})
