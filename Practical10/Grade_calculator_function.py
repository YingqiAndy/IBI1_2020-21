#Grade calculator function
#define the function to calculate grade
def grade_calculator(name, code_portfolio_grade, poster_grade, exam_grade):
    """
    Input:
        name:name of a student ,a string
        code_portfolio_grade: student's code portfolio grade, 40% of the final grade, a positive float
        poster_grade: student's poster presentation grade, 30% of the final grade, a positive float
        exam_grade: student's final exam grade, 30% of the final grade,a positive float
    Return:
        Students name ,a string and final grade a positive float
    """
    final_grade =code_portfolio_grade*0.4 + poster_grade*0.3 +  exam_grade*0.3  #A formula for calculating the final grade
    a=name
    b=' : '
    c=str(final_grade)
    result =a+b+c
    return result
#a example
name_finalgrade = grade_calculator('bob',80,90,100)

#output name and final grade
print(name_finalgrade)