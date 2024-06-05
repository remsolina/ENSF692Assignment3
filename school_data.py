# school_data.py
# AUTHOR NAME Remi Oyediji
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.


import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Declare any global variables needed to store the data here

print("\n***ENSF 692 School Enrollment Statistics***\n")
years = [year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022]
data = np.array(years).reshape(10, 20, 3)
#print(data)

school_codes = ['1224','1679','9626','9806','9813','9815','9816','9823','9825','9826','9829','9830','9836','9847','9850','9856','9857','9858','9860','9865']
school_names = ['Centennial High School', 'Robert Thirsk School', 'Louise Dean School', 'Queen Elizabeth High School', 'Forest Lawn High School', 
                'Crescent Heights High School', 'Western Canada High School', 'Central Memorial High School', 'James Fowler High School', 
                'Ernest Manning High School', 'William Aberhart High School', 'National Sport School', 'Henry Wise Wood High School', 
                'Bowness High School', 'Lord Beaverbrook High School', 'Jack James High School', 'Sir Winston Churchill High School', 
                'Dr. E. P. Scarlett High School', 'John G Diefenbaker High School', 'Lester B. Pearson High School']

schools = dict(zip(school_names,school_codes))

# You may add your own additional classes, functions, variables, etc.
def school_metadata(school_names, school_codes, index):
    print(f"School Name: {school_names[index]}, School Code: {school_codes[index]}")

def get_school_stats(data, index):
        print(f"Mean enrollment for Grade 10: {int(np.nanmean(data[:,index,0]))}")
        print(f"Mean enrollment for Grade 11: {int(np.nanmean(data[:,index,1]))}")
        print(f"Mean enrollment for Grade 12: {int(np.nanmean(data[:,index,2]))}")
        print(f"Highest enrollment for a single grade: {int(np.nanmax(data[:,index,:]))}")
        print(f"Lowest enrollment for a single grade: {int(np.nanmin(data[:,index,:]))}")
        print(f"Total enrollment for 2013: {int(np.nansum(data[0,index,:]))}")
        print(f"Total enrollment for 2014: {int(np.nansum(data[1,index,:]))}")
        print(f"Total enrollment for 2015: {int(np.nansum(data[2,index,:]))}")
        print(f"Total enrollment for 2016: {int(np.nansum(data[3,index,:]))}")
        print(f"Total enrollment for 2017: {int(np.nansum(data[4,index,:]))}")
        print(f"Total enrollment for 2018: {int(np.nansum(data[5,index,:]))}")
        print(f"Total enrollment for 2019: {int(np.nansum(data[6,index,:]))}")
        print(f"Total enrollment for 2020: {int(np.nansum(data[7,index,:]))}")
        print(f"Total enrollment for 2021: {int(np.nansum(data[8,index,:]))}")
        print(f"Total enrollment for 2022: {int(np.nansum(data[9,index,:]))}")
        print(f"Total ten year enrollment: {int(np.nansum(data[:,index,:]))}")
        print(f"Mean total enrollment over 10 years: {int(np.nansum(data[:,index,:])/10)}")

def get_gen_stats(data):
        print(f"Mean enrollment in 2013: {int(np.nanmean(data[0,:,:]))}")
        print(f"Mean enrollment in 2022: {int(np.nanmean(data[-1,:,:]))}")
        print(f"Total graduating class of 2022: {int(np.nansum(data[-1,:,2]))}")
        print(f"Highest enrollment for a single grade: {int(np.nanmax(data[:,:,:]))}")
        print(f"Lowest enrollment for a single grade: {int(np.nanmin(data[:,:,:]))}")

def main():
     
    # Print Stage 1 requirements here
    print("Shape of full data array:", data.shape)
    print("Dimensions of full data array:", data.ndim)

    # Prompt for user input
    while True:
        school_input= input("Enter the high school name or school code: ")
        try: 
            if(school_input not in school_codes) and (school_input not in school_names):
                    raise ValueError ("You must enter a valid school name or code.")       
            else:
                 break

        except ValueError as e:
            print(e)
            continue
    
    if(school_input not in school_codes):
        school_input = schools[school_input]
    index = school_codes.index(school_input)
    #print(index)

    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")
    school_metadata(school_names, school_codes, index)
    get_school_stats(data, index)

    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")
    get_gen_stats(data)

    print(over_500_message if over_500_enrollments.size == 0 else f"For all enrollments over 500, the median value was: {median_over_500}")



if __name__ == '__main__':
    main()

