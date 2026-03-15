"""
[머지 정렬 구현]

문제 설명:
- 머지 정렬(Merge Sort) 알고리즘을 구현합니다.
- 분할 정복(Divide and Conquer) 방식을 사용합니다.
- 배열을 절반으로 나누고, 각각을 정렬한 후 병합합니다.

입력:
- arr: 정렬되지 않은 정수 배열

출력:
- 오름차순으로 정렬된 배열

예제:
입력: [38, 27, 43, 3, 9, 82, 10]
출력: [3, 9, 10, 27, 38, 43, 82]

힌트:
- 배열을 절반으로 분할 (재귀)
- 각 부분을 재귀적으로 정렬
- 정렬된 두 부분을 병합
"""
    while (index1 != len(arr) and index2 != len(arr2))
    if arr1[index1] <= arr2[index2]:
        arr.append(arr1[index1])
    else index1 += 1
        arr.append(arr2[index2]) index += 1
    if index != len(arr1):
        arr.append(arr1[index:])
        if index2 != len(arr2):
            arr.append







# 머지는 합치는 함수
def merge(arr, left, mid, right):
    # 왼쪽과 오른쪽으로 나눠야하니까 왼쪽 배열, 오른쪽 배열 새로 만듦
    # 범위를 left ~ mid / mid+1 ~ right 이렇게 잡을거니까
    # mid까지 포함할거니까 mid+1로 범위 잡음
    left_arr = arr[left:mid]
    right_arr = arr[mid + 1 : right + 1]


    # left_arr와 right_arr를 비교하며 작은 값을 arr에 복사
    while left_idx < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_idx] <= right_arr[right_idx]:
            left_arr.append(left_arr[left_idx])
            left_idx += 1
        else:
            right_arr.append(right_arr[right_idx])
            right_idx += 1

    # left_arr에 남은 원소가 있으면 복사
    while left_idx < len(left_arr)
        arr[k] = left_arr[i]
        left_idx += 1
        

    # right_arr에 남은 원소가 있으면 복사
    while right_index < len(right_arr):
        arr[k] = right_arr[j]
        right_idx += 1

    pass


# 머지소트헬퍼는 쪼개는 함수
def merge_sort_helper(arr, left, right):
    # TODO: base case - left가 right보다 작을 때만 정렬
    # 원소가 2개 이상일 때만 정렬
    if left < right:
        # 중간 지점 계산
        mid = (left + right) // 2

        # 왼쪽 배열 재귀로 돌려서 쪼개고 (배열, 시작점, 미드)
        merge_sort_helper(arr, left, mid)

        # 오른쪽 배열 재귀로 돌려서 쪼개고 (배열, 미드+1, 끝점)
        merge_sort_helper(arr, mid + 1, right)

        # 다 쪼갰으면 합치기 시작
        merge(arr, left, mid, right)
    pass


# 배열이 1이면 이미 정렬된 상태니까 의미없으니 배열의 길이가 1초과일때 정렬 시작
def merge_sort(arr):
    if len(arr) > 1:
        merge_sort_helper(arr, 0, len(arr) - 1)
    return arr


# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    arr1 = [38, 27, 43, 3, 9, 82, 10]
    print("=== 테스트 케이스 1 ===")
    print(f"정렬 전: {arr1}")
    result1 = merge_sort(arr1.copy())
    print(f"정렬 후: {result1}")
    print()

    # 테스트 케이스 2
    arr2 = [12, 11, 13, 5, 6, 7]
    print("=== 테스트 케이스 2 ===")
    print(f"정렬 전: {arr2}")
    result2 = merge_sort(arr2.copy())
    print(f"정렬 후: {result2}")
    print()

    # 테스트 케이스 3: 역순
    arr3 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("=== 테스트 케이스 3: 역순 ===")
    print(f"정렬 전: {arr3}")
    result3 = merge_sort(arr3.copy())
    print(f"정렬 후: {result3}")
    print()

    # 테스트 케이스 4: 중복 원소
    arr4 = [5, 2, 8, 2, 9, 1, 5, 5]
    print("=== 테스트 케이스 4: 중복 원소 ===")
    print(f"정렬 전: {arr4}")
    result4 = merge_sort(arr4.copy())
    print(f"정렬 후: {result4}")
