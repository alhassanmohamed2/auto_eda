from jinja2 import Environment, FileSystemLoader
import shutil


def generate_html(data, filename):
    original = './EDA/template/base_template.html'
    target = f'./EDA/generatedHtml/{filename}.html'

    shutil.copyfile(original, target)

    env = Environment(loader = FileSystemLoader('./') )
    template = env.get_template(target)

    with open(target, 'w') as file:
        file.write(template.render(
            filename = filename,
            data_head = data.head().to_html(),
            data_tail = data.tail().to_html(),
            data_shape = data.shape,
            data_size = data.size,
            data_ndim = data.ndim,
            data_describe = data.describe().to_html(),
            data_sample = data.sample().to_html(),
            data_isnull_sum = data.isnull().sum().to_frame().to_html(),
            data_nunique = data.nunique(),
            data_columns = data.columns,
            data_memory_usage = data.memory_usage().to_frame().to_html(),
            data_duplicated = data.duplicated().sum(),
            # data_value_counts = data.value_counts().to_frame().to_html(),
            # data_corr = data.corr().to_html(),
            data_dtypes = data.dtypes.to_frame().to_html()   
        ))
    
 