#bin/instance -OPlone3 debug

from plone.dexterity.utils import createContentInContainer
import pandas

logos = {'bn':'Barisan Nasional',
         'bjis': 'Barisan Jemaah Islamiah Se-Malaysia',
         'dap': 'Parti Tindakan Demokratik',
         'par': 'Parti Alternative Rakyat',
         'pbds': 'Parti Bansa Dayak Sarawak',
         'pbk': 'Parti Bumi Kenyalang',
         'pbsm': 'Parti Bersama Malaysia',
         'pcm': 'Parti Cinta Malaysia',
         'pcs': 'Parti Cinta Sabah',
         'phrs': 'Parti Harapan Rakyat Sabah',
         'pas': 'Parti Islam Se-Malaysia',
         'pkr': 'Parti Keadilan Rakyat',
         'pkan': 'Parti Kerjasama Anak Negeri',
         'pms': 'Parti Maju Sabah',
         'pnp': 'Penang Front Party',
         'pprs': 'Parti Perpaduan Rakyat Sabah',
         'prgjp': 'Parti Rakyat Gabungan Jaksa Pendamai',
         'prn': 'Parti Reformasi Negeri',
         'prm': 'Parti Rakyat Malaysia',
         'ppsta': 'Parti Solidariti Tanah Airku',
         'pprks': 'Pertubuhan Perpaduan Rakyat Kebangsaan Sabah',
         'psm': 'Parti Sosialis Malaysia',
         'warisan': 'Warisan',
          }

df = pandas.read_csv('scipts/parlimen.csv')

politicians_df = df[['person_name_en','on_behalf_of_name_ms']]

for index,row in politicians_df.iterrows():
    name = row['person_name_en']
    party = row['on_behalf_of_name_ms']

    for key, value in logos.iteritems():
        if party == value:
            print name,key
    
            folder = app.unrestrictedTraverse("Plone3/ms")
            item = createContentInContainer(folder, 
                    'representative', 
                    title=name)


#import transaction; transaction.commit()

