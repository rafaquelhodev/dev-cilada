from cilada import domain


def test_can_insert_classifier(session):
    tem_cafe = domain.Perk(description="Aqui tem café", cilada_points=15)
    casa_do_chefe = domain.Perk(
        description="Escritório na casa do chefe", cilada_points=15
    )

    cilada_classifier = domain.CiladaClassifier(
        perks={tem_cafe, casa_do_chefe}, cilada_threshold=20
    )

    session.add(cilada_classifier)
    session.commit()

    [classifier] = session.execute(
        "SELECT * FROM classifiers WHERE id=:id",
        dict(id=1),
    )

    assert classifier.identifier != None and classifier.identifier != ""
    assert classifier.cilada_threshold == 20


def test_can_query_classifier(session):
    tem_cafe = domain.Perk(description="Aqui tem café", cilada_points=15)
    casa_do_chefe = domain.Perk(
        description="Escritório na casa do chefe", cilada_points=15
    )

    cilada_classifier = domain.CiladaClassifier(
        perks={tem_cafe, casa_do_chefe}, cilada_threshold=20
    )

    session.add(cilada_classifier)
    session.commit()

    classifier = session.query(domain.CiladaClassifier).all()[0]

    assert len(classifier.perks) == 2
