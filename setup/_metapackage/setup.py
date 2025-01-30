import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo9-addons-akretion-automatic-email",
    description="Meta package for akretion-automatic-email Odoo addons",
    version=version,
    install_requires=[
        'odoo9-addon-account_invoice_email',
        'odoo9-addon-action_server_email',
        'odoo9-addon-base_automatic_mail',
        'odoo9-addon-sale_email',
        'odoo9-addon-sale_invoice_email',
        'odoo9-addon-stock_picking_email',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 9.0',
    ]
)
