import os
import sys
from optparse import OptionParser
import string
from collections import defaultdict
import linecache
import itertools
import re

def __init_options__(args):
	parser = OptionParser()
	parser.add_option("-f", "--gitlog_filename",type="string",
					  dest="gitlog_filename",
					  help="gitlog filename which needs to be used for fetching churn count and top committers.")
	parser.add_option("-s", "--gitstatlog_filename",type="string",
					  dest="gitstatlog_filename",
					  help="gitstatlog filename which needs to be used for finding files changed together.")
	(options,args) = parser.parse_args(args)
	return options

def find_files_changed_together(filename):
	commit_2_files = defaultdict(list)
	final_list_of_changed_files_combinations = []
	files_changed_together = []
	with open(filename) as f:
		lines = f.readlines()
		commitid_line_indexes = []
		for line in lines[:500]:
			if line.startswith('commit'):
				commitid_line_indexes.append(lines.index(line))
	#index of commitid list index
	commitid_idx=0
	#print commitid_line_indexes
	for i in range(len(commitid_line_indexes)-1):
		#print commitid_line_indexes[commitid_idx]+1,commitid_line_indexes[commitid_idx+1]
		commitid = lines[commitid_line_indexes[commitid_idx]].strip().split()[1]
		for line in lines[commitid_line_indexes[commitid_idx]+1:commitid_line_indexes[commitid_idx+1]]:
			if re.match('^([A-Za-z\/\d\.\-_]*)\.\w+$',line.strip()):
				commit_2_files[commitid].append(line.strip())
		commitid_idx+=1
	#for key in commit_2_files:
	#	print key,commit_2_files[key]

	#TODO Fisrt arrange all keys of commit_2_files on alphabates then convert to set then iterate it.
	commit_2_files = set([ sorted(key) from key in commit_2_files ])
	for key in commit_2_files:
		print key
		for i in xrange(2,len(commit_2_files[key])+1):
			print i
			for sublist in itertools.combinations(commit_2_files[key],i):
				final_list_of_changed_files_combinations.append(sublist)
		print final_list_of_changed_files_combinations
	for key in final_list_of_changed_files_combinations:
		if final_list_of_changed_files_combinations.count(key)>1:
			files_changed_together.append(key)
	return set(files_changed_together)
		#print commitid_line_indexes

def fetch_churn_counts_and_top_committers(filename):
	ALPHA = string.ascii_letters
	churn_counts = {}
	committer_frequencies = {}
	with open(filename) as f:
		for line in f:
			line = line.strip()
			if len(line.split('\t'))==1 and line.split('\t')[0]!='':
				author = line.strip()
				try:
					if author not in committer_frequencies:
						committer_frequencies[author]=1
					else:
						committer_frequencies[author]+=1
				except StopIteration:
					pass
			else:
				line_contents = line.split('\t')
				if line_contents[0].isdigit():
					filepath = line_contents[2]
					if filepath not in churn_counts:
						churn_counts[filepath]=1
					else:
						churn_counts[filepath]+=1
	return churn_counts,committer_frequencies

def main(args=None):
	arguments_passed = __init_options__(args)
	if not arguments_passed.gitlog_filename:
		print "Please enter a git log filepath(git_log.txt) for fetching churn counts and top committers.."
		sys.exit(2)
	if not arguments_passed.gitstatlog_filename:
		print "Please enter a git stat log filepath(git_stat_log.txt) for finding file changed together.."
		sys.exit(2)

	#Finding churn counts and committer frequencies
	filechange_counts,top_committers_counts = fetch_churn_counts_and_top_committers(arguments_passed.gitlog_filename)
	print "*****TOP CHURN COUNTS*****"
	print sorted(filechange_counts.items(), key=lambda x: (-x[1], x[0]))[:10]
	print "\n*****TOP COMMITTERS AND THEIR COMMIT COUNTS*****"
	print sorted(top_committers_counts.items(), key=lambda x: (-x[1], x[0]))[:10]
	files_changed_together = find_files_changed_together(arguments_passed.gitstatlog_filename)
	print "\n*****FILES CHANGED TOGETHER*****"
	print list(files_changed_together)

if __name__ == '__main__':
	main()	