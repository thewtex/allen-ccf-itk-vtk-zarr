import argparse
import json
import os


def generate_output_path(input_path):
    dir_path = os.path.dirname(input_path)
    file_name = os.path.basename(input_path)
    last_dot = file_name.rindex('.')
    just_name = file_name[:last_dot]
    file_ext = file_name[last_dot:]
    output_file_name = '{0}_viewer{1}'.format(just_name, file_ext)
    return os.path.join(dir_path, output_file_name)


def process_annotation_json(input_file, output_file):
    with open(input_file) as fd:
        annotation_list = json.load(fd)

    output = []
    for idx, annotation in enumerate(annotation_list):
        if annotation:
            output.append([
                idx,
                '{0} ({1})'.format(str(annotation['acronym']), str(annotation['name'])),
            ])

    with open(output_file, 'w') as fd:
        fd.write(json.dumps(output))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('inputfilepath', help='Abolute path to input json file')
    args = parser.parse_args()

    input_file_path = args.inputfilepath
    output_file_path = generate_output_path(input_file_path)

    process_annotation_json(input_file_path, output_file_path)
