# Python-file-explorer(with git) develop by OSS-TEAM-13

<p align="center">
<a href="https://fixed-borogovia-5fe.notion.site/OSS-Team-13-4df2df4655c645a8a7e49e15abbffa3c">
<img src="https://img.shields.io/badge/NOTION-team_page-green?&style=for-the-badge&logo=notion">
</a>
</p>

## Index

- [Project Description](#Project-Description)
- [Installation Guide](#Installation-Guide)
- [Function design and description(v1.0)](#function-design-and-descriptionv10)
- [Function design and description(v2.0)](#function-design-and-descriptionv20)
- [Team Information](#Team-information)
- [About Collaboration](#About-Collaboration)
- [Copyleft / End User License](#copyleft--end-user-license)

## Project Description

This project is a git file browser project that has been expanded by adding Git-related functions to file browsing.

Provides file browsing function by default and provides the following functions.

- `git init`
- `git add`
- `git commit`
- `git rm ` && `git rm --cached`
- `git restore` && `git restore --staged`
- `git mv`
- `git clone from github`

In branch menu we provides with GUI

- `git branch actions(create, delete, rename, checkout, merge)`
- `Commit history about current branch`

In addition to these features, it displays the file status (4 types) according to Git status as an image!

Also It displays git commit history(in branch menu) and more specific information when click commit objects.

More specific information, You can check information in <b>Function design and description</b> tab.

## Installation Guide

### Needs for running

```bash
Python 3.8+
pip (package installer for Python)
platform : mac OS
```

- Installation

```bash\
git clone https://github.com/CAU-OSS-project-practice/OSS-file-manager.git
cd OSS-file-manager
pip install -r requirements.txt
python3 files_new.py
```

- Operate in virtual environment in case of tkinter library error or python version conflict

```bash
python -m venv .venv # .venv crete
source .venv/bin/activate # Run virtual environment
```

- Disable virtual environment

```bash
deactivate
```

## Function design and description(v1.0)

> All photos can be viewed as enlarged images when clicked.😀

<table><tbody>
		<tr>
			<td colspan=3>
				<br>
				<b>File browser function </b><br>
				<br>
			</td>
		</tr>
		<tr>
			<td width="33%">
				<h4 align="center">
				<a href = "https://raw.githubusercontent.com/CAU-OSS-project-practice/OSS-file-manager/develop/data/execution_image/rootdir.png"><img src="/data/execution_image/rootdir.png" width="100%" height="100%">
					</a><br><br> File search starts at the root directory
				</h4>
			</td>
			<td width="33%">
	   			<h4 align="center">
		   		<a href="https://raw.githubusercontent.com/CAU-OSS-project-practice/OSS-file-manager/develop/data/execution_image/in%20folder.png"><img src="/data/execution_image/in folder.png" width="100%" height="100%"></a><br><br>All files and directories contained in the current directory are represented by icons, names, and extensions. </h4></td>
            <td width="33%">
	   			<h4 align="center">
		   		<a href="https://raw.githubusercontent.com/CAU-OSS-project-practice/OSS-file-manager/develop/data/execution_image/double-click.gif"><img src="/data/execution_image/double-click.gif" width="100%" height="100%"></a><br><br>Browsing via double click </h4></td>
		</tr>
</tbody>
</table>

<table><tbody>
		<tr>
			<td colspan=2>
				<br>
				<b>Git init Feature </b><br>
				<br>
			</td>
		</tr>
		<tr>
			<td width="50%">
				<h4 align="center">
<img width="804" alt="git_init_not_git_repo" src="https://github.com/rbgksqkr/react/assets/63959171/ce081f1c-5bf2-4e15-9b47-510bc62a891c">
					</a><br><br>If the directory is not a Git repository -> Activate the init button
				</h4>
			</td>
			<td width="50%">
	   			<h4 align="center">
                      <img width="804" alt="git_init_git_repo" src="https://github.com/rbgksqkr/react/assets/63959171/709a75ea-e70f-43dd-8165-0cbb3f49b41d">
            </a><br><br>For directories that are already Git repositories -> disable init button</h4></td>
		</tr>
</tbody>
</table>

<table><tbody>
		<tr>
			<td colspan=4>
				<br>
				<b>Show file status according to Git status</b><br>
				<br>
			</td>
		</tr>
		<tr>
			<td width="25%">
				<h4 align="center">
				<a href = "https://raw.githubusercontent.com/CAU-OSS-project-practice/OSS-file-manager/develop/data/icon_file_staged.png"><img src="/data/icon_file_staged.png" width="100%" height="100%">
					</a><br><br>Show staged files
				</h4>
			</td>
			<td width="25%">
	   			<h4 align="center">
		   		<a href="https://github.com/CAU-OSS-project-practice/OSS-file-manager/blob/develop/data/icon_file_unstaged.png?raw=true"><img src="/data/icon_file_unstaged.png" width="100%" height="100%"></a><br>Show unstaged (modified) files<br></h4></td>
                <td width="25%">
	   			<h4 align="center">
		   		<a href="https://raw.githubusercontent.com/CAU-OSS-project-practice/OSS-file-manager/develop/data/icon_file.png"><img src="/data/icon_file.png" width="100%" height="100%"></a><br><br>Show committed (unmodified) files</h4></td>
                <td width="25%">
	   			<h4 align="center">
		   		<a href="https://raw.githubusercontent.com/CAU-OSS-project-practice/OSS-file-manager/develop/data/icon_file_both.png"><img src="/data/icon_file_both.png" width="100%" height="100%"></a><br><br>Show staged-unstaged (modified) files</h4></td>
		</tr>
</tbody>
</table>
Stage is divided into 4 types.

1. Staged
2. unstaged (modified)
3. committed (unmodified)
4. staged - unstaged (when a file is changed in the staged state)

Untracked - Staged files ex) When executing the git rm --cached command, untracked is made to work as a priority.

<table><tbody>
		<tr>
			<td colspan=3>
				<br>
				<b>Git add Feature</b><br>
				<br>
			</td>
		</tr>
		<tr>
			<td width="33%">
				<h4 align="center">
          <img width="804" alt="git_add_before" src="https://github.com/rbgksqkr/react/assets/63959171/514aaa4d-1245-4c3c-9b55-1f34f023e8d5">
					<br><br>before file selection
				</h4>
			</td>
			<td width="33%">
				<h4 align="center">
				<img width="804" alt="git_add_one" src="https://github.com/rbgksqkr/react/assets/63959171/6938733f-a031-4093-8bd8-feaff368b5f9">
					<br><br> When one file is selected, only that file can be added.
				</h4>
			</td>
			<td width="33%">
	   			<h4 align="center">
		   		<img width="804" alt="git_add_all" src="https://github.com/rbgksqkr/react/assets/63959171/b8b24523-a693-466e-8962-4a3d4f41daae">
            <br><br>If no files are selected, git add . movement</h4></td>
		</tr>
</tbody>
</table>

<table><tbody>
		<tr>
			<td colspan=2>
				<br>
				<b>Git commit Feature</b><br>
				<br>
			</td>
		</tr>
		<tr>
			<td width="50%">
				<h4 align="center">
<img width="804" alt="git_commit_show_staged_list" src="https://github.com/rbgksqkr/react/assets/63959171/487c96fb-7094-4427-af14-aa05d3cd05da">
          <br><br>shows the list of staged changes
				</h4>
			</td>
			<td width="50%">
	   			<h4 align="center">
<img width="804" alt="git_commit_message" src="https://github.com/rbgksqkr/react/assets/63959171/860d5f44-ff43-40c9-b30a-37d7765bef86">
            <br><br>writing commit message via GUI</h4></td>
		</tr>
</tbody>
</table>

<table><tbody>
		<tr>
			<td colspan=2>
				<br>
				<b>Git restore Feature</b><br>
				<br>
			</td>
		</tr>
		<tr>
			<td width="50%">
	   			<h4 align="center">
		   		<a href="https://raw.githubusercontent.com/CAU-OSS-project-practice/OSS-file-manager/develop/data/execution_image/git_restore_after.png"><img src="/data/execution_image/git_restore_after.png" width="100%" height="100%"></a><br><br>Before Git restore works (shows modified files)</h4></td>
			<td width="50%">
				<h4 align="center">
				<a href = "https://raw.githubusercontent.com/CAU-OSS-project-practice/OSS-file-manager/develop/data/execution_image/git_restore_before.png"><img src="/data/execution_image/git_restore_before.png" width="100%" height="100%">
					</a><br><br>After git restore works (return to pre-commit state)
				</h4>
			</td>
		</tr>
</tbody>
</table>

<table><tbody>
		<tr>
			<td colspan=2>
				<br>
				<b>Git restore --staged Feature</b><br>
				<br>
			</td>
		</tr>
		<tr>
			<td width="50%">
				<h4 align="center">
				<a href = "https://raw.githubusercontent.com/CAU-OSS-project-practice/OSS-file-manager/develop/data/execution_image/git_restore_staged_before.png"><img src="/data/execution_image/git_restore_staged_before.png" width="100%" height="100%">
					</a><br><br>Git restore --staged before operation (staging files)
				</h4>
			</td>
			<td width="50%">
	   			<h4 align="center">
		   		<a href="https://raw.githubusercontent.com/CAU-OSS-project-practice/OSS-file-manager/develop/data/execution_image/git_restore_staged_after.png"><img src="/data/execution_image/git_restore_staged_after.png" width="100%" height="100%"></a><br><br>git restore --staged Return staged files to modified state</h4></td>
		</tr>
</tbody>
</table>

<table><tbody>
		<tr>
			<td colspan=2>
				<br>
				<b>Git rm Feature</b><br>
				<br>
			</td>
		</tr>
		<tr>
			<td width="50%">
				<h4 align="center">
				<a href = "https://raw.githubusercontent.com/CAU-OSS-project-practice/OSS-file-manager/develop/data/execution_image/rm_before.png"><img src="/data/execution_image/rm_after.png" width="100%" height="100%">
					</a><br><br>git rm before
				</h4>
			</td>
			<td width="50%">
	   			<h4 align="center">
		   		<a href="https://raw.githubusercontent.com/CAU-OSS-project-practice/OSS-file-manager/develop/data/execution_image/rm_after.png"><img src="/data/execution_image/rm_after.png" width="100%" height="100%"></a><br><br>git rm after(Deleted and deleted facts from directory are staged) </h4></td>
		</tr>
</tbody>
</table>

<table><tbody>
		<tr>
			<td colspan=2>
				<br>
				<b>Git rm --cached Feature</b><br>
				<br>
			</td>
		</tr>
		<tr>
			<td width="50%">
				<h4 align="center">
				<a href = "https://raw.githubusercontent.com/CAU-OSS-project-practice/OSS-file-manager/develop/data/execution_image/rm%20_cached_before.png"><img src="/data/execution_image/rm _cached_before.png" width="100%" height="100%">
					</a><br><br>git rm --cached before
				</h4>
			</td>
			<td width="50%">
	   			<h4 align="center">
		   		<a href="https://raw.githubusercontent.com/CAU-OSS-project-practice/OSS-file-manager/develop/data/execution_image/rm_cached_after.png"><img src="/data/execution_image/rm_cached_after.png" width="100%" height="100%"></a><br><br>git rm --cached after -> Not deleted from real directory, but deleted (untracked) from git repository</h4></td>
		</tr>
</tbody>
</table>

<table><tbody>
		<tr>
			<td colspan=2>
				<br>
				<b>Git mv Feature</b><br>
				<br>
			</td>
		</tr>
		<tr>
			<td width="50%">
				<h4 align="center">
  <img width="804" alt="git_mv_open_mv_window" src="https://github.com/rbgksqkr/react/assets/63959171/eb0b1047-049b-484a-9a06-e3807984fe8d">
          <br><br>Write file name to change
				</h4>
			</td>
			<td width="50%">
	   			<h4 align="center">
<img width="804" alt="git_mv_rename" src="https://github.com/rbgksqkr/react/assets/63959171/30fd2f03-2777-455e-80df-dfcda1f428c0">
            <br><br>file name change</h4></td>
		</tr>
</tbody>
</table>

## Function design and description(v2.0)

> All photos can be viewed as enlarged images when clicked.😀

New Feature has updated.

1. We updated basic Git branch associated action(Create, Delete, Rename, Checkout).
2. We updated Git merge action
3. And We can also check Git commit history
4. Git clone from Github

Feature 1 , 2 and 3 can be activated through the Branch Menu button.  
Feature No. 3 was implemented by adding a button to the place where v1.0's git-related actions were gathered.

### <b>Feature 1. Branch Associated Action </b><br>

<table><tbody>
		<tr>
			<td colspan=2>
				<b>Branch Create Feature </b><br>
                <br>it asks the user to enter a branch name and then creates a branch with the name
				<br>
			</td>
		</tr>
		<tr>
			<td width="50%">
				<h4 align="center">
				<a href = "https://github.com/realisshomyang/readmetest/blob/main/create1.png?raw=true"><img src="https://github.com/realisshomyang/readmetest/blob/main/create1.png?raw=trueg" width="100%" height="100%">
					</a><br><br> Ask the user to enter a branch name
				</h4>
			</td>
			<td width="50%">
	   			<h4 align="center">
		   		<a href="https://github.com/realisshomyang/readmetest/blob/main/create2.png?raw=true"><img src="https://github.com/realisshomyang/readmetest/blob/main/create2.png?raw=true" width="100%" height="100%"></a><br><br>Branch has Created in Branch List </h4></td>
		</tr>
</tbody>
</table>

<table><tbody>
		<tr>
			<td colspan=3>
				<br>
				<b>Git Delete Feature </b><br>
				<br> it shows the list of branches, asks the user to select one of them, and deletes the selected one
			</td>
		</tr>
		<tr>
			<td width="33%">
				<h4 align="center">
                <a href="https://raw.githubusercontent.com/realisshomyang/readmetest/main/delete1.png"><img src="https://raw.githubusercontent.com/realisshomyang/readmetest/main/delete1.png" width="100%" height="100%"></a>
                <br><br>Shows the list of branches in Branch list GUI
				</h4>
			</td>
			<td width="33%">
	   			<h4 align="center">
                      <a href="https://raw.githubusercontent.com/realisshomyang/readmetest/main/delete2.png"><img src="https://raw.githubusercontent.com/realisshomyang/readmetest/main/delete2.png" width="100%" height="100%"></a><br><br>Ask the user to select one of them</h4></td>
            <td width="33%">
	   			<h4 align="center">
                      <a href="https://raw.githubusercontent.com/realisshomyang/readmetest/main/delete3.png"><img src="https://raw.githubusercontent.com/realisshomyang/readmetest/main/delete3.png" width="100%" height="100%"></a><br><br>branch has deleted</h4></td>
		</tr>
</tbody>
</table>

<table><tbody>
		<tr>
			<td colspan=3>
				<br>
				<b>Git Rename Feature </b><br>
				<br> it shows the list of branches, asks the user to select one of them and to enter a new name, and renames the branch.
			</td>
		</tr>
		<tr>
			<td width="33%">
				<h4 align="center">
                <a href="https://raw.githubusercontent.com/realisshomyang/readmetest/main/rename1.png"><img src="https://raw.githubusercontent.com/realisshomyang/readmetest/main/rename1.png" width="100%" height="100%"></a>
                <br><br>Shows the list of branches in Branch list GUI
				</h4>
			</td>
			<td width="33%">
	   			<h4 align="center">
                      <a href="https://raw.githubusercontent.com/realisshomyang/readmetest/main/rename2.png"><img src="https://raw.githubusercontent.com/realisshomyang/readmetest/main/rename2.png" width="100%" height="100%"></a><br><br>Ask the user selected branch to enter a new name</h4></td>
            <td width="33%">
	   			<h4 align="center">
                      <a href="https://raw.githubusercontent.com/realisshomyang/readmetest/main/rename3.png"><img src="https://raw.githubusercontent.com/realisshomyang/readmetest/main/rename3.png" width="100%" height="100%"></a><br><br>branch has renamed</h4></td>
		</tr>
</tbody>
</table>

<table><tbody>
		<tr>
			<td colspan=3>
				<br>
				<b>Git Checkout Feature</b><br>
				<br>it shows the list of branches, asks the user to select one of them, and checkout the branch.
			</td>
		</tr>
		<tr>
			<td width="33%">
				<h4 align="center">
                 <a href="https://raw.githubusercontent.com/realisshomyang/readmetest/main/checkout1.png"><img src="https://raw.githubusercontent.com/realisshomyang/readmetest/main/checkout1.png" width="100%" height="100%"></a>
                <br><br>Shows the list of branches in Branch list GUI
				</h4>
			</td>
			<td width="33%">
				<h4 align="center">
				 <a href="https://raw.githubusercontent.com/realisshomyang/readmetest/main/checkout2.png"><img src="https://raw.githubusercontent.com/realisshomyang/readmetest/main/checkout2.png" width="100%" height="100%"></a>
					<br><br> asks the user to select one of them
				</h4>
			</td>
			<td width="33%">
	   			<h4 align="center">
                <a href="https://raw.githubusercontent.com/realisshomyang/readmetest/main/checkout3.png"><img src="https://raw.githubusercontent.com/realisshomyang/readmetest/main/checkout3.png" width="100%" height="100%"></a>
            <br><br>checkout the branch.(You can also just double click the branch list's specific branch to checkout)</h4></td>
		</tr>
</tbody>
</table>

<table><tbody>
		<tr>
			<td colspan=3>
				<br>
				<b>Error message windows</b><br>
				<br> If it is not possible to perform the requested action, then report an error message to the user.
                <br>We have two cases
                <br>1. When attempting to delete a current checked out branch
                <br>2. When attempting to rename a selected branch to already exists branch name<br>
                <br>3. When attempting to create a branch that same name with already exists branch
                <br><b>First Case(Try to delete current checked out branch)</b><br> 
			</td>
		</tr>
		<tr>
			<td width="33%">
				<h4 align="center">
                <a href="https://raw.githubusercontent.com/realisshomyang/readmetest/main/derror1.png"><img src="https://raw.githubusercontent.com/realisshomyang/readmetest/main/derror1.png" width="100%" height="100%"></a>
          <br><br>Current branch list(example)
				</h4>
			</td>
			<td width="33%">
				<h4 align="center">
                <a href="https://raw.githubusercontent.com/realisshomyang/readmetest/main/derror2.png"><img src="https://raw.githubusercontent.com/realisshomyang/readmetest/main/derror2.png" width="100%" height="100%"></a>
          <br><br>When attempting to delete a currently checked out branch
				</h4>
			</td>
            <td width="33%">
				<h4 align="center">
                <a href="https://raw.githubusercontent.com/realisshomyang/readmetest/main/derror3.png"><img src="https://raw.githubusercontent.com/realisshomyang/readmetest/main/derror3.png" width="100%" height="100%"></a>
          <br><br>Error message about First case
				</h4>
			</td>
		</tr>
</tbody>
</table>

<table><tbody>
		<tr>
			<td colspan=3>
				<br>
                <br><b>Second Case(Try to rename selected branch to already exist branch)</b><br> 
			</td>
		</tr>
		<tr>
			<td width="33%">
				<h4 align="center">
                <a href="https://raw.githubusercontent.com/realisshomyang/readmetest/main/rerror1.png"><img src="https://raw.githubusercontent.com/realisshomyang/readmetest/main/rerror1.png" width="100%" height="100%"></a>
          <br><br>Current branch list(example)
				</h4>
			</td>
			<td width="33%">
				<h4 align="center">
                <a href="https://raw.githubusercontent.com/realisshomyang/readmetest/main/rerror2.png"><img src="https://raw.githubusercontent.com/realisshomyang/readmetest/main/rerror2.png" width="100%" height="100%"></a>
          <br><br>When attempting to selected branch to already exist branch
				</h4>
			</td>
            <td width="33%">
				<h4 align="center">
                <a href="https://raw.githubusercontent.com/realisshomyang/readmetest/main/rerror3.png"><img src="https://raw.githubusercontent.com/realisshomyang/readmetest/main/rerror3.png" width="100%" height="100%"></a>
          <br><br>Error message about Second case
				</h4>
			</td>
		</tr>
</tbody>
</table>

<table><tbody>
		<tr>
			<td colspan=3>
				<br>
                <br><b>Third Case(Try to create branch that has name same with already existing branch)</b><br> 
			</td>
		</tr>
		<tr>
			<td width="33%">
				<h4 align="center">
                <a href="https://raw.githubusercontent.com/realisshomyang/readmetest/main/cerror1.png"><img src="https://raw.githubusercontent.com/realisshomyang/readmetest/main/cerror1.png" width="100%" height="100%"></a>
          <br><br>Current branch list(example)
				</h4>
			</td>
			<td width="33%">
				<h4 align="center">
                <a href="https://raw.githubusercontent.com/realisshomyang/readmetest/main/cerror2.png"><img src="https://raw.githubusercontent.com/realisshomyang/readmetest/main/cerror2.png" width="100%" height="100%"></a>
          <br><br>When attempting to create branch that has same with already existing branch
				</h4>
			</td>
            <td width="33%">
				<h4 align="center">
                <a href="https://raw.githubusercontent.com/realisshomyang/readmetest/main/cerror3.png"><img src="https://raw.githubusercontent.com/realisshomyang/readmetest/main/cerror3.png" width="100%" height="100%"></a>
          <br><br>Error message about Third case
				</h4>
			</td>
		</tr>
</tbody>
</table>

### <b>Feature 2. Git merge Action </b><br>

<br> We updated the Feature Git merge Action.
<br> We provides a branch list that will be merged to current branch
<br> And after that, by clicking merge button, user can do merge action
<br>There are two option
<br> 1. Fast-forward merge
<br> 2. 3-way-merge

<br> And we show Error message when some error created.

<table><tbody>
		<tr>
			<td colspan=3>
				<br>
				<b>Fast-forward merge</b><br>
				<br>
			</td>
		</tr>
		<tr>
			<td width="33%">
				<h4 align="center">
                <a href="https://raw.githubusercontent.com/realisshomyang/readmetest/main/ffmerge1.png"><img src="https://raw.githubusercontent.com/realisshomyang/readmetest/main/ffmerge1.png" width="100%" height="100%"></a>
          <br><br>provides a branch list that will be merged to current branch
				</h4>
			</td>
			<td width="33%">
				<h4 align="center">
                <a href="https://raw.githubusercontent.com/realisshomyang/readmetest/main/ffmerge2.png"><img src="https://raw.githubusercontent.com/realisshomyang/readmetest/main/ffmerge2.png" width="100%" height="100%"></a>
          <br><br>select branch that will be merged and click merge
				</h4>
			</td>
            <td width="33%">
				<h4 align="center">
                <a href="https://raw.githubusercontent.com/realisshomyang/readmetest/main/ffmerge3.png"><img src="https://raw.githubusercontent.com/realisshomyang/readmetest/main/ffmerge3.png" width="100%" height="100%"></a>
          <br><br>Success message
				</h4>
			</td>
		</tr>
</tbody>
</table>

<table><tbody>
		<tr>
			<td colspan=3>
				<br>
				<b>3-way merge</b><br>
				<br>
			</td>
		</tr>
		<tr>
			<td width="33%">
				<h4 align="center">
                <a href="https://raw.githubusercontent.com/realisshomyang/readmetest/main/3merge1.png"><img src="https://raw.githubusercontent.com/realisshomyang/readmetest/main/3merge1.png" width="100%" height="100%"></a>
          <br><br>provides a branch list that will be merged to current branch
				</h4>
			</td>
			<td width="33%">
				<h4 align="center">
                <a href="https://raw.githubusercontent.com/realisshomyang/readmetest/main/3merge2.png"><img src="https://raw.githubusercontent.com/realisshomyang/readmetest/main/3merge2.png" width="100%" height="100%"></a>
          <br><br>select branch that will be merged and click merge
				</h4>
			</td>
            <td width="33%">
				<h4 align="center">
                <a href="https://raw.githubusercontent.com/realisshomyang/readmetest/main/3merge3.png"><img src="https://raw.githubusercontent.com/realisshomyang/readmetest/main/3merge3.png" width="100%" height="100%"></a>
          <br><br>Success message
				</h4>
			</td>
		</tr>
</tbody>
</table>

<table><tbody>
		<tr>
			<td colspan=4>
				<br>
				<b>Git Merge error messages</b><br>
                <br>In 3-way merge, merge conflict can be generated.
                <br>We provides the user with an error message. and merge abort button to abort merge.
				<br>
			</td>
		</tr>
		<tr>
			<td width="25%">
				<h4 align="center">
                <a href="https://raw.githubusercontent.com/realisshomyang/readmetest/main/merror1.png"><img src="https://raw.githubusercontent.com/realisshomyang/readmetest/main/merror1.png" width="100%" height="100%"></a>
          <br><br>Test environment. conflict exists in hi.txt
				</h4>
			</td>
			<td width="25%">
				<h4 align="center">
                <a href="https://raw.githubusercontent.com/realisshomyang/readmetest/main/merror3.png"><img src="https://raw.githubusercontent.com/realisshomyang/readmetest/main/merror3.png" width="100%" height="100%"></a>
          <br><br>select branch that will be merged and click merge -> Conflict occured!!!!
				</h4>
			</td>
            <td width="25%">
				<h4 align="center">
                <a href="https://github.com/realisshomyang/readmetest/blob/main/merror4.png?raw=true"><img src="https://github.com/realisshomyang/readmetest/blob/main/merror4.png?raw=true" width="100%" height="100%"></a>
          <br><br>We provide abort button to abort merge
				</h4>
			</td>
            <td width="25%">
				<h4 align="center">
                <a href="https://raw.githubusercontent.com/realisshomyang/readmetest/main/merror%20312312.png"><img src="https://raw.githubusercontent.com/realisshomyang/readmetest/main/merror%20312312.png" width="100%" height="100%"></a>
          <br><br>Before/After click abort button
				</h4>
			</td>
		</tr>
</tbody>
</table>

### <b>Feature 3. Git Commit history with Graph </b>

<table><tbody>
		<tr>
			<td colspan=2>
				<br>
                <br><b>Git commit history with Graph</b><br> 
                <br>1. You can check the workflow of the current branch.
                <br>2. When you click commit object in graph, You can check detailed information of commit object.
			</td>
		</tr>
		<tr>
			<td width="50%">
				<h4 align="center">
                <a href="https://raw.githubusercontent.com/realisshomyang/readmetest/main/Untitled%20(9).png"><img src="https://raw.githubusercontent.com/realisshomyang/readmetest/main/Untitled%20(9).png" width="100%" height="100%"></a>
          <br><br>Workflow of current list(example)
				</h4>
			</td>
			<td width="50%">
				<h4 align="center">
                <a href="https://raw.githubusercontent.com/realisshomyang/readmetest/main/Untitled%20(8).png"><img src="https://raw.githubusercontent.com/realisshomyang/readmetest/main/Untitled%20(8).png" width="100%" height="100%"></a>
          <br><br>Can check commit object by click, and more complicated commit graph can be created
				</h4>
			</td>
		</tr>
</tbody>
</table>

### <b>Feature 3. Git Clone from Github</b>

<table><tbody>
		<tr>
			<td colspan=2>
				<br>
				<b>Git Clone from public repository</b><br>
				<br>
			</td>
		</tr>
				<tr>
			<td width="50%">
				<h4 align="center">
					<img width="1434" alt="public_repository" src="https://github.com/CAU-OSS-project-practice/OSS-file-manager/assets/63959171/54947d0b-0de3-404b-8c67-e1c62a7a37ad">
          <br><br>Input public repository address
				</h4>
			</td>
			<td width="50%">
	   			<h4 align="center">
					<img width="1434" alt="after_public_clone" src="https://github.com/CAU-OSS-project-practice/OSS-file-manager/assets/63959171/6bcb7f9a-46cb-48b3-99c7-75597a5faf3d">
            <br><br>After click the clone button, clone the public repository</h4></td>
		</tr>

</tbody>
</table>

<table><tbody>
		<tr>
			<td colspan=3>
				<br>
				<b>Git Clone from private repository</b><br>
				<br>
			</td>
		</tr>
		<tr>
			<td width="33%">
				<h4 align="center">
					<img width="1433" alt="private_input" src="https://github.com/CAU-OSS-project-practice/OSS-file-manager/assets/63959171/498c21b4-2cca-4b45-bf21-4a743a679fe4">
					<br><br>Input private repository address
				</h4>
			</td>
			<td width="33%">
				<h4 align="center">
				<img width="1434" alt="private_repository" src="https://github.com/CAU-OSS-project-practice/OSS-file-manager/assets/63959171/e8490b59-da4f-40de-8cf1-5b19c85196ca">
				<br><br>If it is private repository, you must input your ID and access token
				</h4>
			</td>
			<td width="33%">
	   			<h4 align="center">
		   		<img width="1434" alt="after_private_clone" src="https://github.com/CAU-OSS-project-practice/OSS-file-manager/assets/63959171/8a0f6ef6-44de-4d08-a795-a50e2ab7964e">
				<br><br>After click the clone button, clone the private repository and save your ID and access token
				</h4>
			</td>
		</tr>
</tbody>
</table>

## Team Information

<table width="788">
<thead>
<tr>
<th width="100" align="center">사진</th>
<th width="100" align="center">성명</th>
<th width="150" align="center">담당</th>
<th width="100" align="center">깃허브</th>
<th width="175" align="center">이메일</th>
</tr> 
</thead>

<tbody>
<tr>
<td width="100" align="center">
  <a href="https://github.com/dn7638/dn7638/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=dn7638/dn7638" />
</a>
  </td>
<td width="100" align="center">최우형</td>
<td width="150" align="center">git flow<br>status management according to git status<br>.git subdirectory control<br>test case creation<br>Git commit history Graph</td>
<td width="100" align="center">
	<a href="https://github.com/dn7638">
		<img src="http://img.shields.io/badge/dn7638-655ced?style=social&logo=github"/>
	</a>
</td>
<td width="175" align="center">
	<a href="mailto:dn7638@cau.ac.kr"><img src="https://img.shields.io/static/v1?label=&message=dn7638@cau.ac.kr&color=orange&style=flat-square&logo=gmail"></a>
	</td>
</tr>
<tr>
<td width="100" align="center"><a href="https://github.com/rbgksqkr/rbgksqkr/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=rbgksqkr/rbgksqkr" />
</a>
</a></td>
<td width="100" align="center">박규한</td>
<td width="300" align="center">git init<br>git add<br>git commit<br>git mv<br>Git clone<br>Git branch action(create,delete,rename,checkout)</td>
</td>
<td width="100" align="center">
  	<a href="https://github.com/rbgksqkr">
		<img src="http://img.shields.io/badge/rbgksqkr-655ced?style=social&logo=github"/>
	</a>
</td>
<td width="175" align="center">
	<a href="mailto:rbgks1937@gmail.com"><img src="https://img.shields.io/static/v1?label=&message=rbgks1937@gmail.com&color=green&style=flat-square&logo=gmail"></a>
	</td>
</tr>

<tr>
<td width="100" align="center"><a href="https://github.com/realisshomyang/PS/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=realisshomyang/PS" />
</a></td>
<td width="100" align="center">조명근</td>
<td width="300" align="center">git rm<br>git rm --cached<br>git restore<br>git restore --staged<br>button activation implementation according to git status of selected file<br>Git merge<br>Documentation<br>test(v2.0)</td>
</td>
<td width="100" align="center">
	<a href="https://github.com/realisshomyang">
		<img src="http://img.shields.io/badge/realisshomyang-655ced?style=social&logo=github"/>
	</a>
</td>
<td width="175" align="center">
	<a href="mailto:mgmg612@gmail.com"><img src="https://img.shields.io/static/v1?label=&message=mgmg612@gmail.com&color=green&style=flat-square&logo=gmail"></a>
	</td>
</tr>
</tr>
</tbody>
</table>

## About Collaboration

Tools used for the collaborative development

- [notion](https://bit.ly/3O3sl87)
- [github](https://github.com/CAU-OSS-project-practice/OSS-file-manager)

## Copyleft / End User License

This program is licensed under the Python Software Foundation License (PSF License).
third party softwares that may be contained in this program is referd in license.txt below.

- https://github.com/CAU-OSS-project-practice/OSS-file-manager/blob/main/license
