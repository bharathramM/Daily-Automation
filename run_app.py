import os
import subprocess

app_config = {
    'current_dir_name': { 'port': 3000,
                            'app_type': 'rails',
                            'ruby': '2.4.1',
                            'gemset': 'gemset_name' }                      
}

# Current working Directory Path
cwdp = os.getcwd()
# Parent working Directory Path
pwdp = os.path.abspath('..')

config = app_config.get(os.path.basename(cwdp).replace('-', '_'))

if config:
    if config['app_type'] == 'rails':
        cmd = f'rails s -p {config["port"]} -b 0.0.0.0'
        subprocess.run(cmd, shell=True)
    else:
        print('Please Mention Application Type :(')
else:
    print('Sorry not yet configured :(')
