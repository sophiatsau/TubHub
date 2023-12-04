from flask import Blueprint, session, request
from app.models import Shop, db, Category
from app.forms import ShopCreateForm, ShopUpdateForm
from flask_login import current_user, login_required
from .utils import error_messages, error_message, get_unique_filename, upload_file_to_s3, remove_file_from_s3

shop_routes = Blueprint('shop', __name__)


@shop_routes.route('/')
def get_all_shops():
    """
    Returns all shops available as a list of dictionaries
    """
    shops = Shop.query.all()
    return {"shops": [shop.to_dict() for shop in shops]}


@shop_routes.route('/current')
@login_required
def get_user_shops():
    """
    Returns all current user's shops as a list of dictionaries
    """
    shops = Shop.query.filter(Shop.userId==current_user.id).all()
    return {"shops": [shop.to_dict() for shop in shops]}


@shop_routes.route('/<int:id>')
def get_one_shop(id):
    """
    Queries for and returns shop details by id
    """
    shop = Shop.query.get(id)
    if not shop:
        return error_message("shop", "Shop does not exist"), 404
    return shop.to_dict(scope="detailed")


@shop_routes.route('/new', methods=['POST'])
@login_required
def create_shop():
    """
    Creates a new shop and adds it to the database, returns new shop as dictionary
    """
    form = ShopCreateForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        images = {}

        category_list = form.data['categories'].split(',')
        categories = Category.query.filter(Category.name.in_(category_list)).all()

        if not categories:
            return {"errors":"no cats"}, 400

        for field in ["searchImageUrl","coverImageUrl","businessImageUrl"]:
            img = form.data[field]
            img.filename = get_unique_filename(img.filename)
            upload = upload_file_to_s3(img)

            if "url" not in upload:
                # if no upload key, there was an error uploading.
                return upload, 500

            url = upload["url"]
            images[field]=url

        form_data = {**form.data, **images, "userId": current_user.id}

        del form_data['csrf_token']
        del form_data['categories']

        shop = Shop( **form_data)

        shop.categories.extend(categories)

        db.session.add(shop)
        db.session.commit()
        return shop.to_dict(scope="detailed"), 201
    elif form.errors:
        return error_messages(form.errors), 400
    else:
        return error_message(), 500


@shop_routes.route('/<int:shopId>/edit', methods=['PUT'])
@login_required
def update_shop(shopId):
    """
    Edits an existing shop, returns edited shop as dictionary
    """
    shop = Shop.query.get(shopId)
    print("🚀 ~ file: shop_routes.py:95 ~ shop:", shop)

    # errors
    if not shop:
        return error_message("shop", "Shop not found."), 404
    if shop.userId != current_user.id:
        return error_message("user", "Authorization Error."), 403

    form = ShopUpdateForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    print("🚀 ~ file: shop_routes.py:105 ~ form.data:", form.data)

    if form.validate_on_submit():
        updated_data = {}

        for [field, value] in form.data.items():
            print("🚀 ~ file: shop_routes.py:109 ~ [field, value]:", [field, value])
        return shop


        for field in ["searchImageUrl","coverImageUrl","businessImageUrl"]:
            img = form.data[field]
            if not img:
                continue
            img.filename = get_unique_filename(img.filename)
            upload = upload_file_to_s3(img)

            if "url" not in upload:
                # if no upload key, there was an error uploading.
                return upload, 500

            url = upload["url"]
            updated_data[field]=url

        form_data = {**form.data, **updated_data, "userId": current_user.id}

        del form_data['csrf_token']
        del form_data['categories']

        shop.categories_names
        category_list = form.data['categories'].split(',')
        categories = Category.query.filter(Category.name.in_(category_list)).all()

        shop.categories.extend(categories)

        db.session.add(shop)
        db.session.commit()
        return shop.to_dict(scope="detailed"), 201
    elif form.errors:
        return error_messages(form.errors), 400
    else:
        return error_message(), 500
