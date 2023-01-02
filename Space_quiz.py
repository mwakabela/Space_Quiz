def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct answer! \n")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry, wrong answer, try again. ")
            attempt = attempt + 1
            if attempt == 3:
                print("The correct answer is", answer + "\n")


score = 0
print("*** SPACE QUIZ!!! ***")
print("This quiz has 50 questions. Test your knowledge about Space and Astronomy.")
print("NOTE: You are advised to start your answers with a capital letter. \n")
guess1 = input("1. What is the name of the force which keeps the planets in orbit around the sun? ")
check_guess(guess1, "Gravity")

guess2 = input("2. Which planet is covered by clouds of sulphuric acid? ")
check_guess(guess2, "Venus")

guess3 = input("3. Which planet is named after the Roman god of war? ")
check_guess(guess3, "Mars")

guess4 = input("4. Which planet is closest to the sun? ")
check_guess(guess4, "Mercury")

guess5 = input("5. Which two planets take less time than Earth to orbit the sun? ")
check_guess(guess5, "Mercury and Venus")

guess6 = input("6. Which planet has a day which lasts eight months? ")
check_guess(guess6, "Venus")

guess7 = input("7. What is the term for a natural satellite? ")
check_guess(guess7, "Moon")

guess8 = input("8. Who was the first man in space? ")
check_guess(guess8, "Yuri Gagarin")

guess9 = input("10. Which was the first space probe to leave the solar system?")
check_guess(guess9, "Pioneer 10")

guess10 = input("10. How many US space shuttles are there? ")
check_guess(guess10, "Four")

guess11 = input("11. What is the approximate temperature at the surface of the Sun in celcius?")
check_guess(guess11, "5530")

guess12 = input("12. What force bends light rays travelling though the universe? ")
check_guess(guess12, "Gravity")

guess13 = input("13. What is almost halfway through its 10-billion-year life, will expand to become a red giant and then shrink to become a white dwarf? ")
check_guess(guess13, "Sun")

guess14 = input("14. Which planet orbits the Sun four times in the time it takes the Earth to go round once? ")
check_guess(guess14, "Mercury")

guess15 = input("15. What name was given to the invisible material once thought to occupy all space? ")
check_guess(guess15, "Ether")

guess16 = input("Which is the largest moon in the solar system? ")
check_guess(guess16, "Ganymede")

guess17 = input("17. Where is the Palomar telescope? ")
check_guess(guess17, "Mount Palomar, California")

guess18 = input("18. Where, theoretically, might one find objects squeezed to an infinite density? ")
check_guess(guess18, "Black Hole")

guess19 = input("19. Which is the largest moon of Saturn? ")
check_guess(guess19, "Titan")

guess20 = input("20. Who was the first Cambridge professor of radio astronomy? ")
check_guess(guess20, "Martin Ryle")

guess21 = input("21. Who discovered Uranus? ")
check_guess(guess21, "William Herschel")

guess22 = input("22. Which is the largest planet in the solar system? ")
check_guess(guess22, "Jupiter")

guess23 = input("23. What is the smallest planet in the solar system? ")
check_guess(guess23, "Pluto")

guess24 = input("24. Which is the brightest comet in the solar system? ")
check_guess(guess24, "Halley's comet")

guess25 = input("25. What would you find if you travelled to the centre of the solar system? ")
check_guess(guess25, "The Sun")

guess26 = input("26. How many planets are there in the solar system? ")
check_guess(guess26, "Nine")

guess27 = input("27. Which planet is named after the Roman goddess of love? ")
check_guess(guess27, "Venus")

guess28 = input("28. What kind of extraterrestrial objet has been named after the 17th-century astronomer Edmond Halley? ")
check_guess(guess28, "A Comet")

guess29 = input("29. What was the first artificial satellite? ")
check_guess(guess29, "Sputnik 1")

guess30 = input("30. What is the name of the space shuttle destroyed in midair 28 Jan 1986? ")
check_guess(guess30, "Challenger")

guess31 = input("31. Where is the chromosphere? ")
check_guess(guess31, "Sun")

guess32 = input("32. What, ultimately, will the sun become? ")
check_guess(guess32, "A white dwarf")

guess33 = input("33. Which planet takes almost 30 Earth years to orbit the sun? ")
check_guess(guess33, "Saturn")

guess34 = input("34. What is the most distant object visible to the naked eye? ")
check_guess(guess34, "Andromeda galaxy")

guess35 = input("35. Which planet is the densest? ")
check_guess(guess35, "Earth")

guess36 = input("36. What is the name given to the super dense stars that sometimes result form a supernova? ")
check_guess(guess36, "Neutron Stars")

guess37 = input("37. What is the name of the theory that the universe appears the same wherever and whenever viewed? ")
check_guess(guess37, "Steady-state theory")

guess38 = input("38. Which planet has the Great Red Spot? ")
check_guess(guess38, "Jupiter")

guess39 = input("39. What shape is the Milky Way? ")
check_guess(guess39, "Spiral")

guess40 = input("40. When was the first Pioneer space probe launched? ")
check_guess(guess40, "1958")

guess41 = input("41. Which planet id named after the sky-god who was father of the Titans? ")
check_guess(guess41, "Uranus")

guess42 = input("42. Who was the first living creature in space? ")
check_guess(guess42, "Laika")

guess43 = input("43. Which planet has supersonic winds? ")
check_guess(guess43, "Neptune")

guess44 = input("44. Which planets have no moons? ")
check_guess(guess44, "Mercury and Venus")

guess45 = input("45. Which planet is usually the furthest form the Sun, but sometimes is not? ")
check_guess(guess45, "Pluto")

guess46 = input("46. Which planet is known as the Morning Star? ")
check_guess(guess46, "Venus")

guess47 = input("47. Who was the first woman to travel into space? ")
check_guess(guess47, "Valentina Tereshkova")

guess48 = input("48. What color is Mars’ sunset? ")
check_guess(guess48, "Blue")

guess49 = input("49. What is the name of the brightest start in the night sky? ")
check_guess(guess49, "Sirius")

guess50 = input("50. Who invented astronomy? ")
check_guess(guess50, "Ancient Greeks")

print("Your total score is " + str(score))



