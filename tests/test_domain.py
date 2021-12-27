import pytest

from cilada.domain import Perk, CiladaClassifier, JobProposal


class TestCilada:
    def test_should_not_classify_as_cilada(self):
        tem_cafe = Perk(description="Aqui tem café", cilada_points=15)
        casa_do_chefe = Perk(
            description="Escritório na casa do chefe", cilada_points=15
        )

        cilada_classifier = CiladaClassifier(
            perks={tem_cafe, casa_do_chefe}, cilada_threshold=20
        )

        job_proposal = JobProposal(classifier=cilada_classifier, perks={tem_cafe})

        assert job_proposal.is_cilada() == False

    def test_should_classify_as_cilada(self):
        tem_cafe = Perk(description="Aqui tem café", cilada_points=15)
        casa_do_chefe = Perk(
            description="Escritório na casa do chefe", cilada_points=15
        )

        cilada_classifier = CiladaClassifier(
            perks={tem_cafe, casa_do_chefe}, cilada_threshold=20
        )

        job_proposal = JobProposal(
            classifier=cilada_classifier, perks={tem_cafe, casa_do_chefe}
        )

        assert job_proposal.is_cilada() == True
