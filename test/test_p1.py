import os
import sys


class Cala_p1(object):
    def __init__(self, date, pwd):
        self.date = '20181202'
        self.pwd = "/Users/zxh/rawbuild/result/%s" % date

    def get_all_dirs(self):

        dirs = os.listdir(self.pwd)
        full_dirs = []
        for dir in dirs:
            if os.path.isdir(os.path.join(self.pwd, dir)):
                full_dirs.append(os.path.join(self.pwd, dir))
        return full_dirs

    def get_case_dir(self, dirs):
        if len(dirs) == 0:
            print("images Version dirs list are empty")
            sys.exit(1)

        full_case_dirs = []
        for dir in dirs:
            for case_dir in os.listdir(dir):
                full_case_dirs.append(os.path.join(dir, case_dir))
        return full_case_dirs

    def get_case_file(self, case_dirs):
        if len(case_dirs) == 0:
            print("Case dirs list are empty")
            sys.exit(1)

        filename_index = ".result"
        full_files = []
        for case_dir in case_dirs:
            for filename in os.listdir(case_dir):
                if filename_index in filename:
                    full_files.append(os.path.join(case_dir, filename))

        return full_files

    def read_file(self, full_files):
        if len(full_files) == 0:
            print("Error:read_file() full files list are emprt")
            sys.exit(1)

        result_dict_list = []
        for filename in full_files:
            with open(filename, r) as f:
                file_all_lines = []
                file_all_lines.append(f.readlines)
                tmp_dict = parse_data(f, file_all_lines)
                result_dict_list.append(tmp_dict)
        return result_dict_list

    def parse_data(self, fd, file_all_lines):
        if len(file_all_lines) == 0:
            print("lines list are empty")
            sys.exit(1)

        for file_lines in file_all_lines:
            print(file_lines)
            tmp_dict = {}
            avg_index = "Avg"
            max_index = "Max"
            if len(file_lines) < 6:
                tmp_dict[avg_index] = 0
                tmp_dict[max_index] = 0
            tmp_dict[avg_index] = file_lines[-2].split('=')[-1]  # avg
            tmp_dict[max_index] = file_lines[-1].split('=')[-1]  # max
            tmp_dict["samples"] = file_lines[-3].split('=')[-1]  # samples
            tmp_dict['filename'] = fd.name
            return tmp_dict

    def save_file(self, result_dice_list):
        if len(result_dice_list) == 0:
            print("result_dict_list is empty")
            sys.exit(1)

        result_dict = {}
        i = 0
        while i < len(self, result_dice_list):
            case_name = self.result_dice_list[i]["filename"].split('/')[-2]
            result_dict[case_name] = []
            i += 1

        for result_key in result_dict.keys():
            for tmp_dict in self.result_dict_list:
                filename = tmp_dict['filename']
                if self.result_key == filename.split('/')[-2]:
                    result_dict[result_key].append(tmp_dict)

        filename = "/Users/zxh/rawbuild/result/20190125/result/txt"
        fd = open(self, filename, "w")
        for case_name, values in result_dict.items():
            fd.writelines(case_name + "\n")
            for item in values:
                file_path_list = item["filename"].split("/")
                filename = file_path_list[-3] + "/" + file_path_list[-2] + "/" + file_path_list[-1]
                fd.writelines("\t" + filename + ":\n\t" + "Avg:\t" + item["Avg"] + "\tMax:\t" + item["Max"] + "\n")

            fd.writelines("\n")
            print("文件保存成功！")


def main():
    full_dirs = get_all_dirs()
    case_dirs = get_case_dir(full_dirs)
    full_files = get_case_file(case_dirs)
    result_dict_list = read_file_(full_files)
    save_file(result_dict_list)


if __name__ == '__main__':
    main()
