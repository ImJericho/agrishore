import os
import pandas as pd
import glob

def process_csv_files():
    # Get current directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Find all subfolders in the current directory
    # Define specific folders to process
    folder1 = "Production_Crops_Livestock_E_All_Data"
    folder2 = "Production_Indices_E_All_Data"
    folder3 = "Trade_DetailedTradeMatrix_E_All_Data"
    folder4 = "Value_of_Production_E_All_Data"

    
    if os.path.exists(os.path.join(base_dir, folder1)) and False:
        folder = os.path.join(base_dir, folder1)
        # Find CSV files ending with All_Data.csv in each subfolder
        csv_files = glob.glob(os.path.join(folder, "*All_Data.csv"))
        
        for file_path in csv_files:
            print(f"Processing: {file_path}")
            
            try:
                # Read the CSV file
                df = pd.read_csv(file_path)
                
                # Get original column count
                original_cols = len(df.columns)
                
                code_columns = ['Area Code (M49)','Item Code', 'Element Code']
                code_columns += [f'Y{year}N' for year in range(1900, 2500)]
                code_columns += [f'Y{year}F' for year in range(1900, 2500)]
                df = df.drop(columns=code_columns, errors='ignore')
                
                # Get new column count
                new_cols = len(df.columns)
                
                # Generate output filename (same as input)
                output_path = file_path[:-4]+"_Processed.csv"
                
                # Save the modified DataFrame back to CSV
                df.to_csv(output_path, index=False)
                
                print(f"  Removed {original_cols - new_cols} columns with 'code' in name")
                print(f"  Saved to: {output_path}")
                
            except Exception as e:
                print(f"  Error processing {file_path}: {e}")
    if os.path.exists(os.path.join(base_dir, folder2)) and False:
        folder = os.path.join(base_dir, folder2)
        # Find CSV files ending with All_Data.csv in each subfolder
        csv_files = glob.glob(os.path.join(folder, "*All_Data.csv"))
        
        for file_path in csv_files:
            print(f"Processing: {file_path}")
            
            try:
                # Read the CSV file
                df = pd.read_csv(file_path)
                
                # Get original column count
                original_cols = len(df.columns)
                
                code_columns = ['Area Code (M49)','Item Code', 'Element Code']
                code_columns += [f'Y{year}F' for year in range(1900, 2500)]
                df = df.drop(columns=code_columns, errors='ignore')
                
                # Get new column count
                new_cols = len(df.columns)
                
                # Generate output filename (same as input)
                output_path = file_path[:-4]+"_Processed.csv"
                
                # Save the modified DataFrame back to CSV
                df.to_csv(output_path, index=False)
                
                print(f"  Removed {original_cols - new_cols} columns with 'code' in name")
                print(f"  Saved to: {output_path}")
                
            except Exception as e:
                print(f"  Error processing {file_path}: {e}")
    if os.path.exists(os.path.join(base_dir, folder3)) and False:
        folder = os.path.join(base_dir, folder3)
        # Find CSV files ending with All_Data.csv in each subfolder
        csv_files = glob.glob(os.path.join(folder, "*All_Data.csv"))
        
        for file_path in csv_files:
            print(f"Processing: {file_path}")
            
            try:
                # Read the CSV file
                df = pd.read_csv(file_path)
                
                # Get original column count
                original_cols = len(df.columns)
                
                code_columns = ['Area Code (M49)','Item Code', 'Element Code']
                code_columns += [f'Y{year}F' for year in range(1900, 2500)]
                df = df.drop(columns=code_columns, errors='ignore')
                
                # Get new column count
                new_cols = len(df.columns)
                
                # Generate output filename (same as input)
                output_path = file_path[:-4]+"_Processed.csv"
                
                # Save the modified DataFrame back to CSV
                df.to_csv(output_path, index=False)
                
                print(f"  Removed {original_cols - new_cols} columns with 'code' in name")
                print(f"  Saved to: {output_path}")
                
            except Exception as e:
                print(f"  Error processing {file_path}: {e}")            
    if os.path.exists(os.path.join(base_dir, folder4)) and False:
        folder = os.path.join(base_dir, folder4)
        # Find CSV files ending with All_Data.csv in each subfolder
        csv_files = glob.glob(os.path.join(folder, "*All_Data.csv"))
        
        for file_path in csv_files:
            print(f"Processing: {file_path}")
            
            try:
                # Read the CSV file
                df = pd.read_csv(file_path)
                
                # Get original column count
                original_cols = len(df.columns)
                
                code_columns = ['Area Code (M49)','Item Code', 'Element Code']
                code_columns += [f'Y{year}F' for year in range(1900, 2500)]
                df = df.drop(columns=code_columns, errors='ignore')
                
                # Get new column count
                new_cols = len(df.columns)
                
                # Generate output filename (same as input)
                output_path = file_path[:-4]+"_Processed.csv"
                
                # Save the modified DataFrame back to CSV
                df.to_csv(output_path, index=False)
                
                print(f"  Removed {original_cols - new_cols} columns with 'code' in name")
                print(f"  Saved to: {output_path}")
                
            except Exception as e:
                print(f"  Error processing {file_path}: {e}")
    
    if True:
        folder = os.path.join(base_dir)
        # Find CSV files ending with All_Data.csv in each subfolder
        file_path = "Data/FAOSTAT_data_en_5-22-2025.csv"
        
        print(f"Processing: {file_path}")
        
        try:
            # Read the CSV file
            df = pd.read_csv(file_path)
            
            # Get original column count
            original_cols = len(df.columns)
            # Domain Code,Domain,Reporter Country Code (M49),Reporter Countries,Partner Country Code (M49),Partner Countries,Element Code,Element,Item Code (CPC),Item,Year Code,Year,Unit,Value,Flag,Flag Description

            code_columns = ['Domain Code', 'Domain', 'Reporter Country Code (M49)', 'Partner Country Code (M49)', 'Element Code', 'Item Code (CPC)', 'Year Code', 'Flag', 'Flag Description']
            df = df.drop(columns=code_columns, errors='ignore')
            
            # Get new column count
            new_cols = len(df.columns)
            
            # Generate output filename (same as input)
            output_path = file_path[:-4]+"_Processed.csv"
            
            # Save the modified DataFrame back to CSV
            df.to_csv(output_path, index=False)
            
            print(f"  Removed {original_cols - new_cols} columns with 'code' in name")
            print(f"  Saved to: {output_path}")
            
        except Exception as e:
            print(f"  Error processing {file_path}: {e}")
    print("Processing complete!")

if __name__ == "__main__":
    process_csv_files()