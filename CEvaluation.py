import glob


# 파일 경로 A, B, C, D 따로  
#file_paths = glob.glob("IMU/**/inference_results.txt") # EX) CLASS A라고 생각한 파일만 넣기
file_paths_A = glob.glob("IMU/A/**/inference_results.txt") # EX) CLASS A라고 생각한 파일만 넣기
file_paths_B = glob.glob("IMU/B/**/inference_results.txt") # EX) CLASS A라고 생각한 파일만 넣기
file_paths_C = glob.glob("IMU/C/**/inference_results.txt") # EX) CLASS A라고 생각한 파일만 넣기
file_paths_D = glob.glob("IMU/D/**/inference_results.txt") # EX) CLASS A라고 생각한 파일만 넣기




total_lines = 0
class_a_count = 0
class_b_count = 0
class_c_count = 0
class_d_count = 0


for file_path in file_paths_A:  # file_paths_B file_paths_C file_paths_D
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                class_a_count += line.count('Class A')  
                class_b_count += line.count('Class B') 
                class_c_count += line.count('Class C')  
                class_d_count += line.count('Class D')  
                
                total_lines += 1  
              

    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred while reading {file_path}: {e}")

if total_lines > 0:

    print(f"'Class A': {class_a_count}\n'Class B': {class_b_count}\n'Class C': {class_c_count}\n'Class D': {class_d_count}")

    print(f"class A ratio: {class_a_count / total_lines *100:.2f}%")
    print(f"class B ratio: {class_b_count / total_lines *100:.2f}%")
    print(f"class C ratio: {class_c_count / total_lines *100:.2f}%")
    print(f"class D ratio: {class_d_count / total_lines *100:.2f}%")

else:
    print("No lines to analyze in any files.")