# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['gui.py'],
             pathex=['C:\\Users\\wonsim\\Documents\\hinata_maker'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.datas += [
    ('hajime0.gif', 'C:\\Users\\wonsim\\Documents\\hinata_maker\\hajime0.gif', 'DATA'),
    ('hajime1.gif', 'C:\\Users\\wonsim\\Documents\\hinata_maker\\hajime1.gif', 'DATA'),
    ('sprites\\hajime_right_0.gif', 'C:\\Users\\wonsim\\Documents\\hinata_maker\\sprites\\hajime_right_0.gif', 'DATA'),
    ('sprites\\hajime_right_1.gif', 'C:\\Users\\wonsim\\Documents\\hinata_maker\\sprites\\hajime_right_1.gif', 'DATA'),
    ('sprites\\hajime_left_0.gif', 'C:\\Users\\wonsim\\Documents\\hinata_maker\\sprites\\hajime_left_0.gif', 'DATA'),
    ('sprites\\hajime_left_1.gif', 'C:\\Users\\wonsim\\Documents\\hinata_maker\\sprites\\hajime_left_1.gif', 'DATA'),
]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='hinata_maker',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          icon='C:\\Users\\wonsim\\Documents\\hinata_maker\\hinata_maker.ico',
          console=False )
