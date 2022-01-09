from cilada.domain import Perk, CiladaClassifier, JobProposal
from cilada.repository import ClassifierRepositoryMemory
from cilada.use_cases import ClassifyJobProposal, CreateClassifier, FindClassifier


class TestCreateClassifier:
    def test_create_classifier(self):
        repo = ClassifierRepositoryMemory()

        tem_cafe = Perk(description="Aqui tem café", cilada_points=15)
        casa_do_chefe = Perk(
            description="Escritório na casa do chefe", cilada_points=15
        )

        create_classifier = CreateClassifier(
            perks={tem_cafe, casa_do_chefe}, cilada_threshold=20, repository=repo
        )

        identifier = create_classifier.execute()

        find_classifier = FindClassifier(identifier=identifier, repository=repo)
        classifier = find_classifier.execute()

        assert classifier != None


class TestClassifyJobProposal:
    def test_job_proposal_is_cilada(self):
        repo = ClassifierRepositoryMemory()

        tem_cafe = Perk(description="Aqui tem café", cilada_points=15)
        casa_do_chefe = Perk(
            description="Escritório na casa do chefe", cilada_points=15
        )

        create_classifier = CreateClassifier(
            perks={tem_cafe, casa_do_chefe}, cilada_threshold=20, repository=repo
        )

        identifier = create_classifier.execute()

        find_classifier = FindClassifier(identifier=identifier, repository=repo)

        classify = ClassifyJobProposal(
            repository=repo,
            identifier=identifier,
            perks_uuid={tem_cafe.identifier, casa_do_chefe.identifier},
            classifier_finder=find_classifier,
        )

        is_cilada = classify.execute()
        assert is_cilada == True

    def test_job_proposal_is_not_cilada(self):
        repo = ClassifierRepositoryMemory()

        tem_cafe = Perk(description="Aqui tem café", cilada_points=15)
        casa_do_chefe = Perk(
            description="Escritório na casa do chefe", cilada_points=15
        )

        create_classifier = CreateClassifier(
            perks={tem_cafe, casa_do_chefe}, cilada_threshold=20, repository=repo
        )

        identifier = create_classifier.execute()

        find_classifier = FindClassifier(identifier=identifier, repository=repo)

        classify = ClassifyJobProposal(
            repository=repo,
            identifier=identifier,
            perks_uuid={tem_cafe.identifier},
            classifier_finder=find_classifier,
        )

        is_cilada = classify.execute()
        assert is_cilada == False
