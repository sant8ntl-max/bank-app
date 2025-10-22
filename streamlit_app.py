import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import random

# Bank code mappings (4-letter codes)
BANK_CODES = {
    "State Bank of India": "SBIN",
    "HDFC Bank": "HDFC",
    "ICICI Bank": "ICIC",
    "Axis Bank": "UTIB",
    "Punjab National Bank": "PUNB",
    "Bank of Baroda": "BARB",
    "Canara Bank": "CNRB",
    "Union Bank of India": "UBIN",
    "Bank of India": "BKID",
    "IDBI Bank": "IBKL",
    "Central Bank of India": "CBIN",
    "Indian Bank": "IDIB",
    "Yes Bank": "YESB",
    "Kotak Mahindra Bank": "KKBK",
    "IndusInd Bank": "INDB"
}

# States list
STATES = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
    "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram",
    "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu",
    "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
    "Delhi", "Jammu and Kashmir", "Ladakh"
]

# Sample branches for different states
BRANCHES = {
    "Maharashtra": ["Andheri East", "Bandra West", "Pune Camp", "Nagpur Main", "Thane West"],
    "Karnataka": ["Koramangala", "Indiranagar", "Jayanagar", "Whitefield", "MG Road"],
    "Delhi": ["Connaught Place", "Karol Bagh", "Dwarka", "Rohini", "Saket"],
    "Tamil Nadu": ["T Nagar", "Anna Nagar", "Coimbatore RS Puram", "Madurai Main", "Trichy"],
    "Uttar Pradesh": ["Hazratganj Lucknow", "Gomti Nagar", "Varanasi Cantonment", "Agra Sadar", "Noida Sector 18"],
    "Gujarat": ["Ashram Road Ahmedabad", "SG Highway", "Surat Ring Road", "Vadodara Alkapuri", "Rajkot Main"],
    "West Bengal": ["Park Street Kolkata", "Salt Lake", "Howrah Main", "Siliguri", "Durgapur"],
    "Rajasthan": ["MI Road Jaipur", "C Scheme", "Jodhpur Main", "Udaipur City", "Kota"],
    "Punjab": ["Mall Road Amritsar", "Ludhiana Ferozepur Road", "Jalandhar City", "Patiala", "Mohali"],
    "Telangana": ["Banjara Hills", "Kukatpally", "Secunderabad", "Gachibowli", "Dilsukhnagar"]
}

# Generic branches for states not in the dictionary
GENERIC_BRANCHES = ["Main Branch", "City Center", "Commercial Street", "Market Road", "Industrial Area"]


def display_menu(items, title):
    """Display a numbered menu of items."""
    print(f"\n{'='*50}")
    print(f"{title:^50}")
    print('='*50)
    for idx, item in enumerate(items, 1):
        print(f"{idx}. {item}")
    print(f"{len(items) + 1}. Enter manually")
    print('='*50)


def get_user_choice(items, prompt, allow_manual=True):
    """Get user choice from menu or manual input."""
    while True:
        try:
            choice = input(prompt)
            choice_num = int(choice)
            
            if 1 <= choice_num <= len(items):
                return items[choice_num - 1]
            elif allow_manual and choice_num == len(items) + 1:
                manual_input = input("Enter manually: ").strip()
                if manual_input:
                    return manual_input
                else:
                    print("Invalid input. Please try again.")
            else:
                print(f"Please enter a number between 1 and {len(items) + 1}")
        except ValueError:
            print("Invalid input. Please enter a number.")


def generate_branch_code(bank_name, state, branch_name):
    """Generate a 6-digit branch code based on inputs."""
    # Create a pseudo-random but consistent code based on inputs
    seed_value = sum(ord(c) for c in (bank_name + state + branch_name))
    random.seed(seed_value)
    
    # Generate 6-digit code
    branch_code = random.randint(100000, 999999)
    return str(branch_code)


def generate_ifsc_code(bank_name, state, branch_name, bank_code_dict):
    """Generate complete IFSC code."""
    # Get bank code
    if bank_name in bank_code_dict:
        bank_code = bank_code_dict[bank_name]
    else:
        # Generate bank code from bank name if not in dictionary
        bank_code = ''.join(c.upper() for c in bank_name.split()[0] if c.isalpha())[:4]
        bank_code = bank_code.ljust(4, 'X')  # Pad with X if less than 4 characters
    
    # Generate branch code
    branch_code = generate_branch_code(bank_name, state, branch_name)
    
    # Format: 4-letter bank code + '0' + 6-digit branch code
    ifsc_code = f"{bank_code}0{branch_code}"
    
    return ifsc_code


def main():
    print("\n" + "="*50)
    print("IFSC CODE GENERATOR".center(50))
    print("="*50)
    
    # Step 1: Select Bank
    bank_list = sorted(BANK_CODES.keys())
    display_menu(bank_list, "SELECT BANK")
    bank_name = get_user_choice(bank_list, "\nEnter your choice: ")
    print(f"✓ Selected Bank: {bank_name}")
    
    # Step 2: Select State
    display_menu(STATES, "SELECT STATE")
    state = get_user_choice(STATES, "\nEnter your choice: ")
    print(f"✓ Selected State: {state}")
    
    # Step 3: Select Branch
    available_branches = BRANCHES.get(state, GENERIC_BRANCHES)
    display_menu(available_branches, "SELECT BRANCH")
    branch_name = get_user_choice(available_branches, "\nEnter your choice: ")
    print(f"✓ Selected Branch: {branch_name}")
    
    # Generate IFSC code
    ifsc_code = generate_ifsc_code(bank_name, state, branch_name, BANK_CODES)
    
    # Display result
    print("\n" + "="*50)
    print("GENERATED IFSC CODE".center(50))
    print("="*50)
    print(f"\nBank Name    : {bank_name}")
    print(f"State        : {state}")
    print(f"Branch Name  : {branch_name}")
    print(f"\n{'IFSC CODE':<13}: {ifsc_code}")
    print("\n" + "="*50)
    
    # Option to generate another
    print("\nWould you like to generate another IFSC code?")
    again = input("Enter 'yes' to continue or any other key to exit: ").strip().lower()
    if again == 'yes' or again == 'y':
        main()
    else:
        print("\nThank you for using IFSC Code Generator!")


if __name__ == "__main__":
    main()
