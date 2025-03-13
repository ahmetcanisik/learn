import statistics


first_semester = (34*0.4) + (24*0.6)
second_semester = (50*0.4) + (45*0.6)

print(
    statistics.mean(
        [first_semester, second_semester]
    )
)