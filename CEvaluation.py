import glob

# 활동 카테고리별 파일 경로 패턴
activities = {
    "Class A": "IMU/**/*_0/**/inference_results.txt",
    "Class B": "IMU/**/*_1/**/inference_results.txt",
    "Class C": "IMU/**/*_2/**/inference_results.txt",
    "Class D": "IMU/**/*_3/**/inference_results.txt"
}

total_lines = 0

correct_counts = {'Class A': 0, 'Class B': 0, 'Class C': 0, 'Class D': 0}
total_counts = {'Class A': 0, 'Class B': 0, 'Class C': 0, 'Class D': 0}

# 파일 처리
for activity, pattern in activities.items():
    file_paths = glob.glob(pattern)
    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                total_lines += len(lines)
                total_counts[activity] += len(lines)
                # 이 부분은 파일 내용에 따라 다르게 조정할 수 있습니다.
                # 예를 들어, 파일 내 각 라인이 "0(walk)"와 같이 레이블링된다고 가정합니다.
                correct_counts[activity] += sum(1 for line in lines if activity in line)

        except FileNotFoundError:
            print(f"The file {file_path} does not exist.")
        except Exception as e:
            print(f"An error occurred while reading {file_path}: {e}")

# 전체 정확도 계산
total_correct = sum(correct_counts.values())
overall_accuracy = total_correct / total_lines if total_lines > 0 else 0

# 결과 출력
print(f"Overall accuracy: {overall_accuracy * 100:.2f}%")
for activity in activities.keys():
    if total_counts[activity] > 0:
        accuracy = correct_counts[activity] / total_counts[activity]
        print(f"Accuracy of {activity}: {accuracy* 100:.2f}%")
    else:
        print(f"Accuracy of {activity}: No data")


