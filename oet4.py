mobile = int(0)
total_result = 0
def display_menu():
    print("Select a category:")
    print("1. CD/DPL/LSL")
    print("2. RELP")
    print("3. TW")
    print("4. DGSL")

def display_buckets(category):
    buckets = {
        1: [f"Bucket {i}" for i in range(1, 8)],  # CD/DPL/LSL
        2: [f"Bucket {i}" for i in range(1, 8)],  # RELP
        3: [f"Bucket {i}" for i in range(1, 8)],  # TW
        4: [f"Bucket {i}" for i in range(1, 6)]   # DGSL
    }
    
    print(f"Select a bucket for category {category}:")
    for i, bucket in enumerate(buckets[category], start=1):
        print(f"{i}. {bucket}")

def display_percentage_options_1(category, bucket):
    percentages = {
        
            1: {1: [13.00, 14.00, 16.00, 17.00],
            2: [6.00, 6.00, 7.00, 8.00],
            3: [5.00, 6.00, 7.00, 8.00],
            4: [4.00, 5.00, 6.00, 7.00],
            5: [00.00, 00.00, 00.00, 00.00],
            6: [00.00, 00.00, 00.00, 00.00],
            7: [00.00, 00.00, 00.00, 00.00]
           },
        2: {1: [12.00, 14.00, 16.00, 18.00],
            2: [6.00, 8.00, 10.00, 11.00],
            3: [6.00, 8.00, 10.00, 11.00],
            4: [4.00, 5.00, 6.00, 7.00],
            5: [00.00, 00.00, 00.00, 00.00],
            6: [00.00, 00.00, 00.00, 00.00],
            7: [00.00, 00.00, 00.00, 00.00]
           },
        3: {1: [13.00, 14.00, 16.00, 17.00],
            2: [6.00, 8.00, 10.00, 11.00],
            3: [5.00, 6.00, 7.00, 8.00],
            4: [4.00, 5.00, 6.00, 7.00],
            5: [00.00, 00.00, 00.00, 00.00],
            6: [00.00, 00.00, 00.00, 00.00],
            7: [00.00, 00.00, 00.00, 00.00]
           },
        4: {1: [12.00, 13.00, 15.00, 17.00],
            2: [4.00, 6.00, 8.00, 9.00],
            3: [00.00, 00.00, 00.00, 00.00],
            4: [00.00, 00.00, 00.00, 00.00],
            5: [00.00, 00.00, 00.00, 00.00]
           }
    }
    print(f"Select a percentage for Bucket {bucket}:")
    for i, perc in enumerate(percentages[category][bucket], start=1):
        print(f"{i}. {perc:.2f}%")

def display_percentage_options_3(category, bucket):
    percentages = {
        1: {1: [76.00, 79.00, 81.00, 86.00],
            2: [18.00, 20.00, 22.00, 24.00],
            3: [14.00, 17.00, 20.00, 22.00],
            4: [10.00, 12.00, 14.00, 16.00],
            5: [1.90, 2.40, 2.90, 3.40],
            6: [1.40, 1.90, 2.40, 2.90],
            7: [1.10, 1.60, 2.10, 2.60]
           },
        2: {1: [86.00, 88.00, 91.00, 92.00],
            2: [31.00, 36.00, 41.00, 46.00],
            3: [26.00, 31.00, 36.00, 41.00],
            4: [21.00, 22.00, 23.00, 27.00],
            5: [2.00, 2.75, 3.50, 4.50],
            6: [1.75, 2.50, 3.00, 3.50],
            7: [1.50, 1.75, 2.00, 2.75]
           },
        3: {1: [89.00, 91.00, 92.00, 93.00],
            2: [66.00, 71.00, 76.00, 81.00],
            3: [41.00, 46.00, 51.00, 56.00],
            4: [31.00, 36.00, 41.00, 46.00],
            5: [5.00, 6.00, 7.00, 8.00],
            6: [4.00, 5.00, 6.00, 7.00],
            7: [3.00, 3.50, 4.00, 4.50]
           },
        4: {1: [70.00, 71.00, 73.00, 78.00],
            2: [16.00, 19.00, 21.00, 23.00],
            3: [11.00, 13.00, 15.00, 17.00],
            4: [8.00, 11.00, 13.00, 16.00],
            5: [1.80, 2.30, 2.80, 3.80]
           }
    }
    
    

    print(f"Select a percentage for Bucket {bucket}:")
    for i, perc in enumerate(percentages[category][bucket], start=1):
        print(f"{i}. {perc:.2f}%")

def calculate_overall_res_payout(integer_input, fixed_percentage):
    global total_result  # Declare total_result as global
    print(f'1. fees collection <125')
    print(f'2. fees collection is 150')
    print(f"3. fees collection is 0")
    fees = int(input("Enter the option 1 or 2 or 3: "))
    
    mobile = int(input("Enter the extra amount: "))
    
    if fees == 1:
        result = (((fixed_percentage / 100) * integer_input) - ((2 / 100) * integer_input) + mobile)
    elif fees == 2:
        result = (((fixed_percentage / 100) * integer_input) + ((2 / 100) * integer_input) + mobile)
    elif fees == 3:
        result = (((fixed_percentage / 100) * integer_input) + mobile)
    else:
        print("Enter a valid input.")
        return
    
    print(f"Result of Overall Res Payout calculation at {fixed_percentage}%: {result}")
    
    if total_result == 0:
        total_result = result  # Set total_result to the first result if it was zero
    else:
        total_result += result  # Otherwise, add the result to total_result

    print(f"Current total result: {total_result}")

def calculate_Normalization_Target(fixed_percentage_1, integer_input, fixed_percentage):
    global total_result  # Declare total_result as global
    print(f'1. fees collection <125')
    print(f'2. fees collection is 150')
    print(f"3. fees collection is 0")
    fees = int(input("Enter the option 1 or 2 or 3: "))
    
    mobile = int(input("Enter the extra amount: "))
    
    if fees == 1:
        result = ((fixed_percentage / 100) * integer_input)
    elif fees == 2:
        result = ((fixed_percentage / 100) * integer_input)
    elif fees == 3:
        result = ((fixed_percentage / 100) * integer_input)
    else:
        print("Enter a valid input.")
        return
    
    final = (fixed_percentage_1 / 100) * integer_input
    final_1 = (final + result) + mobile

    print(f"Result of Overall Res Payout calculation at {fixed_percentage_1}%: {final_1:.2f}")

    if total_result == 0:
        total_result = final_1  # Set total_result to the first result if it was zero
    else:
        total_result += final_1  # Otherwise, add the result to total_result

    print(f"Current total result: {total_result}")

def process_bucket(option, integer_input, selected_percentage, category, bucket):
    payout_percentages = {
        1: {76.00: 5.00, 79.00: 6.00, 81.00: 7.00, 86.00: 8.00},
        2: {18.00: 6.00, 20.00: 7.00, 22.00: 8.00, 24.00: 9.00},
        3: {14.00: 7.00, 17.00: 8.00, 20.00: 9.00, 22.00: 10.00},
        4: {10.00: 8.00, 12.00: 9.00, 14.00: 10.00, 16.00: 10.00},
        5: {1.90: 11.00, 2.40: 12.00, 2.90: 13.00, 3.40: 14.00},
        6: {1.40: 11.00, 1.90: 12.00, 2.40: 13.00, 2.90: 14.00},
        7: {1.10: 12.00, 1.60: 13.00, 2.10: 14.00, 2.60: 15.00}
    }
    
    relp_payout_percentages = {
        1: {86.00: 5.00, 88.00: 6.00, 91.00: 7.00, 92.00: 8.00},
        2: {31.00: 6.00, 36.00: 7.00, 41.00: 8.00, 46.00: 9.00},
        3: {26.00: 7.00, 31.00: 8.00, 36.00: 8.00, 41.00: 9.00},
        4: {21.00: 8.00, 22.00: 9.00, 23.00: 10.00, 27.00: 11.00},
        5: {2.00: 10.00, 2.75: 11.00, 3.50: 12.00, 4.50: 13.00},
        6: {1.75: 11.00, 2.50: 12.00, 3.00: 13.00, 3.50: 14.00},
        7: {1.50: 11.00, 1.75: 12.00, 2.00: 13.00, 2.75: 14.00}
    }
    
    tw_payout_percentages = {
        1: {89.00: 6.00, 91.00: 7.00, 92.00: 8.00, 93.00: 9.00},
        2: {66.00: 7.00, 71.00: 8.00, 76.00: 9.00, 81.00: 10.00},
        3: {41.00: 8.00, 46.00: 9.00, 51.00: 10.00, 56.00: 11.00},
        4: {31.00: 9.00, 36.00: 10.00, 41.00: 11.00, 46.00: 12.00},
        5: {5.00: 10.00, 6.00: 11.00, 7.00: 12.00, 8.00: 13.00},
        6: {4.00: 11.00, 5.00: 12.00, 6.00: 13.00, 7.00: 14.00},
        7: {3.00: 12.00, 3.50: 13.00, 4.00: 14.00, 4.50: 15.00}
    }
    
    dgsl_payout_percentages = {
        1: {70.00: 6.00, 71.00: 7.00, 73.00: 8.00, 78.00: 9.00},
        2: {16.00: 7.00, 19.00: 8.00, 21.00: 9.00, 23.00: 10.00},
        3: {11.00: 10.00, 13.00: 11.00, 15.00: 12.00, 17.00: 13.00},
        4: {8.00: 11.00, 11.00: 12.00, 13.00: 13.00, 16.00: 14.00},
        5: {1.80: 12.00, 2.30: 13.00, 2.80: 14.00, 3.80: 15.00}
    }
    payout_percentages_1 = {
        1: {76.00: 13.00, 79.00: 14.00, 81.00: 16.00, 86.00: 17.00},
        2: {18.00: 5.00, 20.00: 6.00, 22.00: 7.00, 24.00: 8.00},
        3: {14.00: 5.00, 17.00: 6.00, 20.00: 7.00, 22.00: 8.00},
        4: {10.00: 4.00, 12.00: 5.00, 14.00: 6.00, 16.00: 7.00},
        5: {1.90: 0.00, 2.40: 0.00, 2.90: 0.00, 3.40: 0.00},
        6: {1.40: 0.00, 1.90: 0.00, 2.40: 0.00, 2.90: 0.00},
        7: {1.10: 0.00, 1.60: 0.00, 2.10: 0.00, 2.60: 0.00}
    }
    relp_payout_percentages_1 = {
        1: {86.00: 12.00, 88.00: 14.00, 91.00: 16.00, 92.00: 18.00},
        2: {31.00: 6.00, 36.00: 8.00, 41.00: 10.00, 46.00: 11.00},
        3: {26.00: 6.00, 31.00: 8.00, 36.00: 10.00, 41.00: 11.00},
        4: {21.00: 4.00, 22.00: 5.00, 23.00: 6.00, 27.00: 7.00},
        5: {2.00: 00.00, 2.75: 00.00, 3.50: 00.00, 4.50: 00.00},
        6: {1.75: 00.00, 2.50: 00.00, 3.00: 00.00, 3.50: 00.00},
        7: {1.50: 00.00, 1.75: 00.00, 2.00: 00.00, 2.75: 00.00}
    }
    tw_payout_percentages_1 = {
        1: {89.00: 13.00, 91.00: 14.00, 92.00: 16.00, 93.00: 17.00},
        2: {66.00: 6.00, 71.00: 8.00, 76.00: 10.00, 81.00: 11.00},
        3: {41.00: 5.00, 46.00: 6.00, 51.00: 7.00, 56.00: 8.00},
        4: {31.00: 4.00, 36.00: 5.00, 41.00: 6.00, 46.00: 7.00},
        5: {5.00: 0.00, 6.00: 0.00, 7.00: 0.00, 8.00: 0.00},
        6: {4.00: 0.00, 5.00: 0.00, 6.00: 0.00, 7.00: 0.00},
        7: {3.00: 0.00, 3.50: 0.00, 4.00: 0.00, 4.50: 0.00}
    }
    
    dgsl_payout_percentages_1 = {
        1: {70.00: 12.00, 71.00: 13.00, 73.00: 15.00, 78.00: 17.00},
        2: {16.00: 4.00, 19.00: 6.00, 21.00: 8.00, 23.00: 9.00},
        3: {11.00: 0.00, 13.00: 0.00, 15.00: 0.00, 17.00: 0.00},
        4: {8.00: 0.00, 11.00: 0.00, 13.00: 0.00, 16.00: 0.00},
        5: {1.80: 0.00, 2.30: 0.00, 2.80: 0.00, 3.80: 0.00}
    }
    payout_percentages_2 = {
        1: {76.00: 0.50, 79.00: 1.00, 81.00: 1.50, 86.00: 2.50},
        2: {18.00: 0.50, 20.00: 1.00, 22.00: 7.00, 24.00: 8.00},
        3: {14.00: 0.50, 17.00: 1.00, 20.00: 7.00, 22.00: 8.00},
        4: {10.00: 0.50, 12.00: 1.00, 14.00: 6.00, 16.00: 7.00},
        5: {1.90: 0.00, 2.40: 0.00, 2.90: 0.00, 3.40: 0.00},
        6: {1.40: 0.00, 1.90: 0.00, 2.40: 0.00, 2.90: 0.00},
        7: {1.10: 0.00, 1.60: 0.00, 2.10: 0.00, 2.60: 0.00}
    }
    relp_payout_percentages_2 = {
        1: {86.00: 1.00, 88.00: 1.50, 91.00: 2.00, 92.00: 3.00},
        2: {31.00: 1.00, 36.00: 1.50, 41.00: 2.00, 46.00: 3.00},
        3: {26.00: 1.00, 31.00: 1.50, 36.00: 2.00, 41.00: 3.00},
        4: {21.00: 1.00, 22.00: 1.50, 23.00: 2.00, 27.00: 3.00},
        5: {2.00: 00.00, 2.75: 00.00, 3.50: 00.00, 4.50: 00.00},
        6: {1.75: 00.00, 2.50: 00.00, 3.00: 00.00, 3.50: 00.00},
        7: {1.50: 00.00, 1.75: 00.00, 2.00: 00.00, 2.75: 00.00}
    }
    tw_payout_percentages_2 = {
        1: {89.00: 1.00, 91.00: 1.50, 92.00: 2.00, 93.00: 3.00},
        2: {66.00: 1.00, 71.00: 1.50, 76.00: 2.00, 81.00: 3.00},
        3: {41.00: 1.00, 46.00: 1.50, 51.00: 2.00, 56.00: 3.00},
        4: {31.00: 1.00, 36.00: 1.50, 41.00: 2.00, 46.00: 3.00},
        5: {5.00: 0.00, 6.00: 0.00, 7.00: 0.00, 8.00: 0.00},
        6: {4.00: 0.00, 5.00: 0.00, 6.00: 0.00, 7.00: 0.00},
        7: {3.00: 0.00, 3.50: 0.00, 4.00: 0.00, 4.50: 0.00}
    }
    
    dgsl_payout_percentages_2 = {
        1: {70.00: 1.00, 71.00: 1.50, 73.00: 2.00, 78.00: 3.00},
        2: {16.00: 1.00, 19.00: 1.50, 21.00: 2.00, 23.00: 3.00},
        3: {11.00: 0.00, 13.00: 0.00, 15.00: 0.00, 17.00: 0.00},
        4: {8.00: 0.00, 11.00: 0.00, 13.00: 0.00, 16.00: 0.00},
        5: {1.80: 0.00, 2.30: 0.00, 2.80: 0.00, 3.80: 0.00}
    }

    payout_percentages_3 = {
        1: {13.00: 0.50, 14.00: 1.00, 16.00: 1.50, 17.00: 2.50},
        2: {5.00: 0.50, 6.00: 1.00, 7.00: 7.00, 8.00: 8.00},
        3: {5.00: 0.50, 6.00: 1.00, 7.00: 7.00, 8.00: 8.00},
        4: {4.00: 0.50, 5.00: 1.00, 6.00: 6.00, 7.00: 7.00},
        5: {0.00: 0.00, 0.00: 0.00, 0.00: 0.00, 0.00: 0.00},
        6: {0.00: 0.00, 0.00: 0.00, 0.00: 0.00, 0.00: 0.00},
        7: {0.00: 0.00, 0.00: 0.00, 0.00: 0.00, 0.00: 0.00}
    }
    relp_payout_percentages_3 = {
        1: {12.00: 1.00, 14.00: 1.50, 16.00: 2.00, 18.00: 3.00},
        2: {6.00: 1.00, 8.00: 1.50, 10.00: 2.00, 11.00: 3.00},
        3: {6.00: 1.00, 8.00: 1.50, 10.00: 2.00, 11.00: 3.00},
        4: {4.00: 1.00, 5.00: 1.50, 6.00: 2.00, 7.00: 3.00},
        5: {0.00: 00.00, 0.00: 00.00, 0.00: 00.00, 0.00: 00.00},
        6: {0.00: 00.00, 0.00: 00.00, 0.00: 00.00, 0.00: 00.00},
        7: {0.00: 00.00, 0.00: 00.00, 0.00: 00.00, 0.00: 00.00}
    }
    tw_payout_percentages_3 = {
        1: {13.00: 1.00, 14.00: 1.50, 16.00: 2.00, 17.00: 3.00},
        2: {6.00: 1.00, 8.00: 1.50, 10.00: 2.00, 11.00: 3.00},
        3: {5.00: 1.00, 6.00: 1.50, 7.00: 2.00, 8.00: 3.00},
        4: {4.00: 1.00, 5.00: 1.50, 6.00: 2.00, 7.00: 3.00},
        5: {0.00: 0.00, 00.00: 0.00, 00.00: 0.00, 00.00: 0.00},
        6: {0.00: 0.00, 00.00: 0.00, 00.00: 0.00, 00.00: 0.00},
        7: {0.00: 0.00, 00.00: 0.00, 00.00: 0.00, 00.00: 0.00}
    }
    
    dgsl_payout_percentages_3 = {
        1: {12.00: 1.00, 13.00: 1.50, 16.00: 2.00, 17.00: 3.00},
        2: {04.00: 1.00, 06.00: 1.50, 08.00: 2.00, 9.00: 3.00},
        3: {00.00: 0.00, 00.00: 0.00, 00.00: 0.00, 00.00: 0.00},
        4: {00.00: 0.00, 00.00: 0.00, 00.00: 0.00, 00.00: 0.00},
        5: {00.00: 0.00, 00.00: 0.00, 00.00: 0.00, 00.00: 0.00}
    }


    percentage_map = {
        1: payout_percentages,
        2: relp_payout_percentages,
        3: tw_payout_percentages,
        4: dgsl_payout_percentages
    }
    percentage1_map = {
        1: payout_percentages_1,
        2: relp_payout_percentages_1,
        3: tw_payout_percentages_1,
        4: dgsl_payout_percentages_1

    }
    percentage2_map = {
        1: payout_percentages_2,
        2: relp_payout_percentages_2,
        3: tw_payout_percentages_2,
        4: dgsl_payout_percentages_2

    }
    percentage3_map = {
        1: payout_percentages_3,
        2: relp_payout_percentages_3,
        3: tw_payout_percentages_3,
        4: dgsl_payout_percentages_3
    }
    if option == 1:
        print("Calculating Overall Res Payout...")
        fixed_percentage = percentage_map.get(category, {}).get(bucket, {}).get(selected_percentage)
        
        if fixed_percentage is None:
            print("Invalid percentage.")
            return
        
        calculate_overall_res_payout(integer_input, fixed_percentage)
        
    
    elif option == 2:

        display_percentage_options_1(category, bucket)
        percentage_option = int(input("Enter percentage option number (1-4): "))

        if percentage_option not in range(1, 5):
                    print("Invalid percentage option.")
    

        percentages = {
                    1: [76.00, 79.00, 81.00, 86.00],
                    2: [18.00, 20.00, 22.00, 24.00],
                    3: [14.00, 17.00, 20.00, 22.00],
                    4: [10.00, 12.00, 14.00, 16.00],
                    5: [1.90, 2.40, 2.90, 3.40],
                    6: [1.40, 1.90, 2.40, 2.90],
                    7: [1.10, 1.60, 2.10, 2.60]
                }
        if category == 2:
                    percentages = {
                        1: [86.00, 88.00, 91.00, 92.00],
                        2: [31.00, 36.00, 41.00, 46.00],
                        3: [26.00, 31.00, 36.00, 41.00],
                        4: [21.00, 22.00, 23.00, 27.00],
                        5: [2.00, 2.75, 3.50, 4.50],
                        6: [1.75, 2.50, 3.00, 3.50],
                        7: [1.50, 1.75, 2.00, 2.75]
                    }
        elif category == 3:
                    percentages = {
                        1: [89.00, 91.00, 92.00, 93.00],
                        2: [66.00, 71.00, 76.00, 81.00],
                        3: [41.00, 46.00, 51.00, 56.00],
                        4: [31.00, 36.00, 41.00, 46.00],
                        5: [5.00, 6.00, 7.00, 8.00],
                        6: [4.00, 5.00, 6.00, 7.00],
                        7: [3.00, 3.50, 4.00, 4.50]
                    }
        elif category == 4:
                    percentages = {
                        1: [70.00, 71.00, 73.00, 78.00],
                        2: [16.00, 19.00, 21.00, 23.00],
                        3: [11.00, 13.00, 15.00, 17.00],
                        4: [8.00, 11.00, 13.00, 16.00],
                        5: [1.80, 2.30, 2.80, 3.80]
                    }


        selected_percentage_2 = percentages[bucket][percentage_option - 1]
        
        
        if percentage_option not in range(1, 5):
            print("Invalid percentage option.")
            return
        print("Calculating Normalization Target...")
        fixed_percentage = percentage_map.get(category, {}).get(bucket, {}).get(selected_percentage)
        
        if fixed_percentage is None:
            print("Invalid percentage.")
            return
        
        fixed_percentage_1 = percentage2_map.get(category, {}).get(bucket, {}).get(selected_percentage_2)
        
        if fixed_percentage_1 is None:
            print("Invalid percentage.")
            return
        
        calculate_Normalization_Target(fixed_percentage_1, integer_input, fixed_percentage)
        
        

def main():

    while True:
        

        display_menu()
        try:
            
            category = int(input("Enter category number (1-4): "))
            if category not in [1, 2, 3, 4]:
                print("Invalid category. Please select a number between 1 and 4.")
                continue

            display_buckets(category)
            num_buckets = int(input("How many buckets do you want to select? "))
            selected_buckets = []

            for _ in range(num_buckets):
                bucket = int(input("Enter bucket number: "))
                max_buckets = 7 if category in [1, 2, 3] else 5

                if bucket < 1 or bucket > max_buckets:
                    print(f"Invalid bucket. Please select a number between 1 and {max_buckets}.")
                    continue

                selected_buckets.append(bucket)

            


            for bucket in selected_buckets:
                 integer_input = int(input(f"Enter an integer value for Bucket {bucket}: "))
                 display_percentage_options_3(category, bucket)
                 percentage_option = int(input("Enter percentage option number (1-4): "))
                 if percentage_option not in range(1, 5):
                        print("Invalid percentage option.")
                        continue

                 percentages = {
                        1: [76.00, 79.00, 81.00, 86.00],
                        2: [18.00, 20.00, 22.00, 24.00],
                        3: [14.00, 17.00, 20.00, 22.00],
                        4: [10.00, 12.00, 14.00, 16.00],
                        5: [1.90, 2.40, 2.90, 3.40],
                        6: [1.40, 1.90, 2.40, 2.90],
                        7: [1.10, 1.60, 2.10, 2.60]
                    }
                 if category == 2:
                        percentages = {
                            1: [86.00, 88.00, 91.00, 92.00],
                            2: [31.00, 36.00, 41.00, 46.00],
                            3: [26.00, 31.00, 36.00, 41.00],
                            4: [21.00, 22.00, 23.00, 27.00],
                            5: [2.00, 2.75, 3.50, 4.50],
                            6: [1.75, 2.50, 3.00, 3.50],
                            7: [1.50, 1.75, 2.00, 2.75]
                        }
                 elif category == 3:
                        percentages = {
                            1: [89.00, 91.00, 92.00, 93.00],
                            2: [66.00, 71.00, 76.00, 81.00],
                            3: [41.00, 46.00, 51.00, 56.00],
                            4: [31.00, 36.00, 41.00, 46.00],
                            5: [5.00, 6.00, 7.00, 8.00],
                            6: [4.00, 5.00, 6.00, 7.00],
                            7: [3.00, 3.50, 4.00, 4.50]
                        }
                 elif category == 4:
                        percentages = {
                            1: [70.00, 71.00, 73.00, 78.00],
                            2: [16.00, 19.00, 21.00, 23.00],
                            3: [11.00, 13.00, 15.00, 17.00],
                            4: [8.00, 11.00, 13.00, 16.00],
                            5: [1.80, 2.30, 2.80, 3.80]
                        }
                    
                 selected_percentage = percentages[bucket][percentage_option - 1]
                    
                 print("Select an option:")
                 print("1. Overall Res Payout")
                 print("2. Normalization Target")

                
                    
                 option = int(input("Enter option number (1-2): "))
                 if option not in [1, 2]:
                        print("Invalid option. Please select 1 or 2.")
                        continue
                  
                    
                 process_bucket(option, integer_input, selected_percentage, category, bucket)
            print(f"Total Overall Result from selected buckets: {total_result:.2f}")
                
            
            
        except ValueError:
            print("Invalid input. Please enter a valid number.")

        cont = input("Do you want to select another category? (yes/no): ").strip().lower()
        if cont != 'yes':
            break

if __name__ == "__main__":
    main()
