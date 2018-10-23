import pandas as pd
import unittest

from matminer.datasets.tests import DataSetTest
from matminer.datasets.convenience_loaders import load_glass_ternary_hipt, \
    load_castelli_perovskites, load_flla, load_boltztrap_mp, \
    load_citrine_thermal_conductivity, load_dielectric_constant, \
    load_double_perovskites_gap, load_double_perovskites_gap_lumo, \
    load_elastic_tensor, load_glass_ternary_landolt, \
    load_phonon_dielectric_mp, load_piezoelectric_tensor, load_mp


class ConvenienceLoadersTest(DataSetTest):
    def test_load_glass_ternary_hipt(self):
        df = load_glass_ternary_hipt()
        self. assertTrue(isinstance(df, pd.DataFrame))

        with self.assertRaises(AttributeError):
            df = load_glass_ternary_hipt(system="Nonexistent system")

        df = load_glass_ternary_hipt(system="CoFeZr")
        self.assertEqual(len(df.index), 1295)

        df = load_glass_ternary_hipt(system=["CoFeZr", "CoTiZr"])
        self.assertEqual(len(df.index), 2576)

    def test_load_castelli_peroskites(self):
        df = load_castelli_perovskites()
        self.assertTrue(isinstance(df, pd.DataFrame))

    def test_load_flla(self):
        df = load_flla()
        self.assertTrue(isinstance(df, pd.DataFrame))

    def test_load_boltztrap_mp(self):
        df = load_boltztrap_mp()
        self.assertTrue(isinstance(df, pd.DataFrame))

    def test_load_citrine_thermal_conductivity(self):
        df = load_citrine_thermal_conductivity(room_temperature=False)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(len(df), 872)

        df = load_citrine_thermal_conductivity(room_temperature=True)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(len(df), 295)

    def test_load_double_perovskites_gap(self):
        df = load_double_perovskites_gap()
        self.assertTrue(isinstance(df, pd.DataFrame))

        df = load_double_perovskites_gap(return_lumo=True)
        self.assertTrue(isinstance(df, tuple))

    def test_load_double_perovskites_gap_lumo(self):
        df = load_double_perovskites_gap_lumo()
        self.assertTrue(isinstance(df, pd.DataFrame))

    def test_load_dielectric_constant(self):
        df = load_dielectric_constant()
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(len(df.columns), 13)

        df = load_dielectric_constant(include_metadata=True)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(len(df.columns), 16)

    def test_load_piezoelectric_tensor(self):
        df = load_piezoelectric_tensor()
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(len(df.columns), 10)

        df = load_piezoelectric_tensor(include_metadata=True)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(len(df.columns), 13)

    def test_load_elastic_tensor(self):
        df = load_elastic_tensor()
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(len(df.columns), 17)

        df = load_elastic_tensor(include_metadata=True)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(len(df.columns), 20)

    def test_load_glass_ternary_landolt(self):
        df = load_glass_ternary_landolt()
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(len(df), 6118)

        df = load_glass_ternary_landolt(unique_composition=False)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(len(df), 7191)

        df = load_glass_ternary_landolt(processing="meltspin")
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(len(df), 5736)

        df = load_glass_ternary_landolt(processing="sputtering")
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(len(df), 403)

        with self.assertRaises(ValueError):
            df = load_glass_ternary_landolt(processing="spittering")

    def test_load_phonon_dielectric_mp(self):
        df = load_phonon_dielectric_mp()
        self.assertTrue(isinstance(df, pd.DataFrame))

    # Skip due to memory usage
    @unittest.skip
    def test_mp(self):
        df = load_mp()
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(len(df.columns), 9)

        df = load_mp(include_structures=True)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(len(df.columns), 11)
