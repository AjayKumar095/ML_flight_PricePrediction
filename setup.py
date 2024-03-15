import setuptools

with open("README.md", 'r') as file:
    long_description =file.read()
  
  
_version_= '0.0.0'
source_name='AeroPredict'
repo_name="ML_Flight_Price_Project"
Author_name='AjayKumar095'
Author_Email='jaykumar002kori@gmail.com'

HYPEN_E_DOT='-e.'

def get_requirements(file_path):
   
    with open(file_path, 'r') as file:
        data=file.read()
        
        if data :
            data=data.replace('\n', ' ')
            data=data.split()
            if HYPEN_E_DOT in data or '' in data :
                data.remove(HYPEN_E_DOT)
        
        return data    



setuptools.setup(
    name=source_name,
    version=_version_,
    author=Author_name,
    author_email=Author_Email,
    install_requires=get_requirements("requirements.txt"),
    description='A small python package for ML Apps.',
    long_description=long_description,
    
    url=f'https://github.com/{Author_name}/{repo_name}',
    project_urls={
        "Bug Tracker" : f'https://github.com/{Author_name}/{repo_name}/issues'
    },
    
    packages=setuptools.find_packages()
    
)    