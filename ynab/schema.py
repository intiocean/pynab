# -*- coding: utf-8 -*-

from schematics.models import Model
from schematics.types import BooleanType, StringType, FloatType, DateType, IntType
from schematics.types.compound import ListType, ModelType


class Device(Model):
    highestDataVersionImported = StringType()
    friendlyName = StringType()
    hasFullKnowledge = BooleanType()
    lastDataVersionFullyKnown = StringType()
    shortDeviceId = StringType()
    formatVersion = StringType()
    knowledgeInFullBudgetFile = StringType()
    YNABVersion = StringType()
    deviceGUID = StringType()
    deviceType = StringType()
    knowledge = StringType()
    deviceVersion = StringType()


class Entity(Model):
    entityId = StringType()
    entityType = StringType()
    entityVersion = StringType()
    isTombstone = BooleanType()


class Category(Entity):
    name = StringType()
    sortableIndex = IntType()
    type = StringType()


class SubCategory(Category):
    cachedBalance = FloatType()
    masterCategoryId = StringType()
    isResolvedConflict = BooleanType()
    note = StringType()


class MasterCategory(Category):
    deleteable = BooleanType()
    expanded = BooleanType()
    subCategories = ListType(ModelType(SubCategory))


class Account(Entity):
    accountName = StringType()
    accountType = StringType()
    hidden = BooleanType()
    onBudget = BooleanType()
    lastReconciledDate = DateType()
    lastReconciledBalance = FloatType()
    lastEnteredCheckNumber = FloatType()
    sortableIndex = IntType()
    note = StringType()


class MonthlySubCategoryBudget(Entity):
    budgeted = FloatType()
    categoryId = StringType()
    overspendingHandling = StringType()
    parentMonthlyBudgetId = StringType()


class MonthlyBudget(Entity):
    month = DateType()
    monthlySubCategoryBudgets = ListType(ModelType(MonthlySubCategoryBudget))


class PayeeLocation(Entity):
    parentPayeeId = StringType()
    latitude = FloatType()
    longitude = FloatType()
    isResolvedConflict = BooleanType()


class PayeeRenameConditions(Entity):
    parentPayeeId = StringType()
    operand = StringType()
    operator = StringType()


class Payee(Entity):
    name = StringType()
    enabled = BooleanType()
    autoFillAmount = FloatType()
    autoFillCategoryId = StringType()
    autoFillMemo = StringType()
    targetAccountId = StringType()
    renameConditions = ListType(ModelType(PayeeRenameConditions))
    locations = ListType(ModelType(PayeeLocation))


class TransactionEntity(Entity):
    memo = StringType()
    amount = FloatType()
    transferTransactionId = StringType()
    categoryId = StringType()
    targetAccountId = StringType()
    isResolvedConflict = BooleanType()


class SubTransaction(TransactionEntity):
    parentTransactionId = StringType()


class Transaction(TransactionEntity):
    date = DateType()
    cleared = StringType()
    accepted = BooleanType()
    dateEnteredFromSchedule = DateType()
    accountId = StringType()
    payeeId = StringType()
    subTransactions = ListType(ModelType(SubTransaction))
