import pytest

from lemonsqueezy.api.customer import (
    create_customer,
    get_customer,
    list_customers,
    update_customer,
)
from lemonsqueezy.api.errors import LemonSqueezyClientError
from lemonsqueezy.models import Customer, CustomerCreate, CustomerList, CustomerPatch


@pytest.fixture
def customer_create():
    return CustomerCreate(
        data=CustomerCreate.Data(
            type="customers",
            attributes=CustomerCreate.Data.Attributes(
                name="John Doe",
                email="johndoe@example.com",
                city="New York",
                region="NY",
                country="US",
            ),
            relationships=CustomerCreate.Data.Relationships(
                store=CustomerCreate.Data.Relationships.Store(
                    data=CustomerCreate.Data.Relationships.Store.StoreData(
                        type="stores", id="1"
                    )
                )
            ),
        )
    )


@pytest.fixture
def customer_patch():
    return CustomerPatch(
        data=CustomerPatch.Data(
            type="customers",
            id="1",
            attributes=CustomerPatch.Data.Attributes(
                name="John Doe", email="johndoe@example.com", status="archived"
            ),
        )
    )


@pytest.mark.skip("Not implemented due to lack of valid store data.")
def test_create_customer(customer_create):
    customer = create_customer(customer_create)
    assert isinstance(customer, Customer)


@pytest.mark.skip("Not implemented due to lack of valid customer data.")
def test_get_customer():
    customer = get_customer("1")
    assert isinstance(customer, Customer)


def test_get_customer_invalid():
    with pytest.raises(LemonSqueezyClientError) as exc_info:
        get_customer("1")

    assert exc_info.value.status_code == 404


@pytest.mark.skip("Not implemented due to lack of valid customer data.")
def test_update_customer(customer_patch):
    customer = update_customer(customer_patch)
    assert isinstance(customer, Customer)


def test_list_customers():
    customers = list_customers()
    assert all(isinstance(customer, CustomerList) for customer in customers)
