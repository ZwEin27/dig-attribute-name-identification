
import os
import data_loader
import identifier


def run(root_dir):
    df_paths = data_loader.load_domain_file_paths(root_dir)
    for (domain_name, filepath_list) in df_paths.items():
        path = os.path.join(root_dir, domain_name, 'attribute_name_mapping.json')
        identifier.identify(filepath_list, output=path)
        break

if __name__ == '__main__':
    run('../../dig-data/sample-datasets/escorts/')