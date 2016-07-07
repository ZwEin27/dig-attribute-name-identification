
import os
import data_loader
import identifier


def run(root_dir):
    df_paths = data_loader.load_domain_file_paths(root_dir)
    for (domain_name, filepath_list) in df_paths.items():
        for filepath in filepath_list: 
            path = os.path.join('/'.join(filepath.split('/')[:-1]), 'attribute_name_mapping.json')
            identifier.identify(filepath, output=path)
        break

if __name__ == '__main__':
    run('../../dig-data/sample-datasets/escorts/')