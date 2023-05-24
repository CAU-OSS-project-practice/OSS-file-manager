import tkinter as tk
from collections import deque
from tkinter import ttk
import pygit2

# Git 리포지토리 경로
repo_path = "/Users/wh/Documents/Zoom/OSS-file-manager"

# Git 리포지토리 열기
repo = pygit2.Repository(repo_path)


# 커밋 히스토리 그래프 생성 함수
def draw_commit_history():
    window = tk.Tk()
    window.title("Commit History Graph")

    # 프레임 생성
    left = tk.Frame(window, border=1, relief="flat", bg="white")
    left.pack(side="left", fill="both", expand=True)

    right = tk.Frame(window, border=1, relief="flat", bg="white", width='40')
    right.pack(side="left", fill="y")

    # 스크롤바
    scrollbar_left = ttk.Scrollbar(left, orient="vertical")
    scrollbar_left.pack(side="right", fill="y")

    scrollbar_right = ttk.Scrollbar(right, orient="vertical")
    scrollbar_right.pack(side="right", fill="y")

    # Treeview 생성
    tree = ttk.Treeview(right, columns=("#0"), selectmode="extended", show="tree headings")
    tree.heading("#0", text="commit", anchor="w")
    tree.column("#0", anchor="e", stretch=False, width=300)
    tree.pack(side="left", fill="y")

    # 캔버스
    canvas = tk.Canvas(left, bg="white", yscrollcommand=scrollbar_left.set)
    canvas.pack(fill="both", expand=True)

    # left 영역의 스크롤바와 캔버스 연결
    scrollbar_left.config(command=canvas.yview)

    # right 영역의 스크롤바와 캔버스 연결
    scrollbar_right.config(command=canvas.yview)

    # 내용 프레임
    content_frame = tk.Frame(canvas, bg="white")
    content_frame.pack(fill="both", expand=True)
    canvas.create_window((0, 0), window=content_frame, anchor="nw")

    # 각 행의 높이
    row_height = 20

    commits = []  # 커밋 객체 리스트
    num_of_commit = 0
    for row, commit in enumerate(repo.walk(repo.head.target, pygit2.GIT_SORT_TOPOLOGICAL | pygit2.GIT_SORT_TIME)):
        commits.append(commit)  # 커밋 ID를 행 번호로 등록
        num_of_commit = row

    parent_list = deque()

    for i in range(0, len(commits)):
        next_commit_id = str()
        row = i + 1
        if i != 0:
            col = parent_list.index(str(commits[i].id)[0:7])
        elif i == 0:
            col = 0
            parent_list.append(str(commits[0].id)[0:7])
        alive_parent = len(parent_list)
        print("--------------loop-------------------------")
        print("현재 커밋 아이디 : ", commits[i].id)
        print("현재 커밋의 패런트 아이디 : ", commits[i].parent_ids)
        print("현재 parent 데크 목록 : ", parent_list)
        print("현재 column : ", col)
        print("현재 row : ", row)
        # 여기에 점 찍기

        node_width = 50
        node_height = 15
        node_x = 60
        node_y = row_height + (row_height - node_height) // 2
        canvas.create_rectangle(node_x * col, node_y * row, node_x * col + node_width, node_y * row + node_height,
                                fill="lightblue",
                                outline="black")
        canvas.create_text(node_x * col + node_width // 2, node_y * row + node_height // 2,
                           text=str(commits[i].id)[0:7])

        if i < len(commits) - 1:
            next_commit_id = str(commits[i + 1].id)[0:7]

        # parent_list 업데이트
        temp_list = reversed(commits[i].parent_ids)
        for j in temp_list:
            parent_list.insert(col, str(j)[0:7])
        print(parent_list)
        count = 0
        while True:
            try:
                parent_list.remove(str(commits[i].id)[0:7])
                print("[", str(commits[i].id)[0:7], "] removed!!!!!!!!!!!")
                count += 1
            except ValueError:
                break
        print("다음 parent 데크 목록 (선긋기): ", parent_list)
        # 다음거 체크
        branch_pair = []
        next_col = str()
        check_next = 0
        temp_cnt = 0
        if i < len(commits) - 1:
            next_col = parent_list.index(str(commits[i + 1].id)[0:7])
        for j in range(len(parent_list)):
            if len(commits[i].parents) == 2:
                if parent_list[j] == next_commit_id:
                    # 여기 페어에 연결
                    if j == parent_list.index(str(commits[i].parent_ids[0])[0:7]) + 1:
                        branch_pair.append([col, next_col])
                        temp_cnt += 1
                        print("???")
                    else:
                        branch_pair.append([j - temp_cnt, next_col])
                    check_next += 1
                else:
                    if parent_list[j] == str(commits[i].parent_ids[1])[0:7]:
                        temp_cnt += 1
                        branch_pair.append([j - temp_cnt, j])
                    else:
                        branch_pair.append([j - temp_cnt, j - temp_cnt])
                    # 그냥 일직선
            else :
                if parent_list[j] == next_commit_id:
                    branch_pair.append([j, next_col])
                    check_next += 1
                else:
                    if check_next > 1:
                        branch_pair.append([j, j - check_next + 1])
                    else:
                        branch_pair.append([j, j])
                    # 그냥 일직선
        temp_index = 0
        count = 0
        if check_next > 1:
            while True:
                try:
                    if count == 0:
                        temp_index = parent_list.index(str(commits[i + 1].id)[0:7])
                    parent_list.remove(str(commits[i + 1].id)[0:7])
                    count += 1
                except ValueError:
                    parent_list.insert(temp_index, str(commits[i + 1].id)[0:7])
                    break
            for x, y in branch_pair:
                # branch pair row, x -> row + 1 , y 로 선긋기
                # 좌표 정보 node_x * col, node_y * row
                canvas.create_line(node_x * (x), node_y * row, node_x * (y), node_y * (row + 1), fill="black")
        else:
            if len(commits[i].parents) == 2:
                for j in range(col + 1):
                    canvas.create_line(node_x * j, node_y * row, node_x * j, node_y * (row + 1), fill="black")
                for j in range(col, alive_parent):
                    canvas.create_line(node_x * j, node_y * row, node_x * (j + 1), node_y * (row + 1), fill="black")
            elif len(commits[i].parents) == 1:
                for j in range(alive_parent):
                    canvas.create_line(node_x * j, node_y * row, node_x * j, node_y * (row + 1), fill="black")

        # 커밋 데이터를 행마다 그리기
        tree.insert("", tk.END, text=str(commits[i].id)[0:5], values=[
            row], open=False)

    def configure_canvas(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    canvas.bind("<Configure>", configure_canvas)

    window.mainloop()


# 커밋 히스토리 그리기
draw_commit_history()
